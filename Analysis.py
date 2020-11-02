import numpy as np
import cv2
from scipy.ndimage import label
from scipy import ndimage
from PIL import Image
from skimage.feature import peak_local_max
from skimage.draw import circle_perimeter
import math

class ImageAnalyzer(object):
    
    def __init__(self,analysisgui, inout_resource_gui):
        self.AnalysisGui = analysisgui
        self.inout_resource_gui = inout_resource_gui

    def neuceli_segmenter(self, input_img, pixpermic=None):
        
        if self.AnalysisGui.NucDetectMethod.currentText() == "Int.-based Processing":
            
#             if np.asarray(pixpermic).astype('float') > 0.3:
#                 scale_factor = math.ceil(np.asarray(pixpermic).astype('float')/0.3)
#                 newsize = scale_factor * input_img.shape
#                 np.resize(input_img,newsize) 
            
            first_tresh = self.AnalysisGui.NucFirstThresholdSlider.value()*2.55
            second_thresh = 255-(self.AnalysisGui.NucSecondThresholdSlider.value()*2.55)
            Cell_Size = self.AnalysisGui.NucleiAreaSlider.value()
                
            boundary, mask = self.segmenter_function(input_img, cell_size=Cell_Size, 
                                                     first_threshold=first_tresh, second_threshold=second_thresh)
            
#             if np.asarray(pixpermic).astype('float') > 0.3:
#                 old_size = input_img.shape
#                 np.resize(mask,old_size) 
#                 np.resize(boundary,old_size) 
            
            
            
        return boundary, mask   
    
    def segmenter_function(self, input_img, cell_size=None, first_threshold=None, second_threshold=None):
    
        img_uint8 = cv2.copyMakeBorder(input_img,5,5,5,5,cv2.BORDER_CONSTANT,value=0)
        
        
        ## First blurring round
        if (cell_size %2)==0:
            cell_size = cell_size + 1
        median_img = cv2.medianBlur(img_uint8,cell_size)
        gaussian_blurred = cv2.GaussianBlur(median_img,(5,5),0)
        ## Threhsolding and Binarizing
        ret, thresh = cv2.threshold(gaussian_blurred,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        bin_img = (1-thresh/255).astype('bool')
        ## Binary image filling
        filled = ndimage.binary_fill_holes(bin_img)
        filled_int= (filled*255).astype('uint8')
        ## Gray2RGB to feed the watershed algorithm
        img_rgb  = cv2.cvtColor(img_uint8,cv2.COLOR_GRAY2RGB)
        boundary = img_rgb
        boundary = boundary - img_rgb
        ## Distance trasform and thresholing to set the watershed markers
        dt = cv2.distanceTransform(filled.astype(np.uint8), 2, 3)
        dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(np.uint8)
        _, dt = cv2.threshold(dt, first_threshold, 255, cv2.THRESH_BINARY)
        lbl, ncc = label(dt)
        lbl = lbl * (255 / (ncc + 1))
        lbl = lbl.astype(np.int32)
        ## First round of Watershed transform
        cv2.watershed(img_rgb, lbl)
        ## Correcting image boundaries
        boundary[lbl == -1] = [255,255,255]
        boundary[0,:] = 0
        boundary[-1,:] = 0
        boundary[:,0] = 0
        boundary[:, -1] = 0
        b_gray = cv2.cvtColor(boundary,cv2.COLOR_BGR2GRAY)
        diff = filled_int-b_gray

        kernel = np.ones((11,11), np.uint8)
        first_pass = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)

        ## Second round of marker generation and watershed 
        kernel = np.ones((5,5),np.uint8)
        aa = first_pass.astype('uint8')
        erosion = cv2.erode(aa,kernel,iterations = 1)
        kernel = np.ones((11,11), np.uint8)
        opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
        blur = cv2.GaussianBlur(opening,(11,11),50)
        ret2, thresh2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        dt = cv2.distanceTransform(255-thresh2, 2, 3)
        dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(np.uint8)
        _, dt = cv2.threshold(dt, second_threshold, 255, cv2.THRESH_BINARY)
        lbl, ncc = label(dt)
        lbl = lbl * (255 / (ncc + 1))
        lbl = lbl.astype(np.int32)
        cv2.watershed(img_rgb, lbl)
        ########
        boundary = img_rgb
        boundary = boundary - img_rgb

        boundary[lbl == -1] = [255,255,255]
        boundary_img = boundary[3:boundary.shape[0]-3,3:boundary.shape[1]-3]
        bound_gray = cv2.cvtColor(boundary_img,cv2.COLOR_BGR2GRAY)
        resized_bound = cv2.resize(bound_gray,(input_img.shape[1],input_img.shape[0]))

        kernel = np.ones((3,3),np.uint8)
        boundary = cv2.dilate(resized_bound,kernel,iterations = 1)
        filled1 = ndimage.binary_fill_holes(boundary)
        fin= 255*filled1-boundary
        mask = ndimage.binary_fill_holes(fin)
        mask = (255*mask).astype(np.uint8)

        return boundary, mask
            
    
    
    def max_z_project(self, image_stack):
        
        z_imglist=[]
        
        for index, row in image_stack.iterrows():
            im = Image.open(row['ImageName'])
            z_imglist.append( np.asarray(im))
        z_stack = np.stack(z_imglist, axis=2)
        max_project = z_stack.max(axis=2)
        
        return max_project
    
   
    
    def SpotDetector(self, input_image, AnalysisGui, nuclei_image):
        
        uint8_max_val = 255
    
        ## First blurring round
        median_img = cv2.medianBlur(nuclei_image,11)
        ## Threhsolding and Binarizing
        ret, thresh = cv2.threshold(median_img,0,uint8_max_val,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        bin_img = (1-thresh/uint8_max_val).astype('bool')
        ## Binary image filling
        filled = ndimage.binary_fill_holes(bin_img)
        struct = ndimage.generate_binary_structure(2, 2)
        filled = ndimage.binary_dilation(filled, structure=struct).astype(filled.dtype)
        filled = ndimage.binary_dilation(filled, structure=struct).astype(filled.dtype)
        masked_input = np.multiply(input_image,filled)
        
        sig=3
        if str(AnalysisGui.spotanalysismethod.currentIndex()) == '0':
            
            log_result = ndimage.gaussian_laplace(masked_input, sigma=sig)
            
            if str(AnalysisGui.thresholdmethod.currentIndex()) == '0':
                
                ret_log, thresh_log = cv2.threshold(log_result,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
                
            elif str(AnalysisGui.thresholdmethod.currentIndex()) == '1':
                
                manual_threshold = AnalysisGui.ThresholdSlider.value()*2.55
                ret_log, thresh_log = cv2.threshold(log_result,0,255,cv2.THRESH_BINARY_INV+manual_threshold)
                
            bin_img_log = (1-thresh_log/255).astype('bool')
            spots_img_log = (bin_img_log*255).astype('uint8')
            kernel = np.ones((3,3), np.uint8)
            spot_openned_log = cv2.morphologyEx(spots_img_log, cv2.MORPH_OPEN, kernel)
            final_spots = spot_openned_log
            
        elif str(AnalysisGui.spotanalysismethod.currentIndex()) == '1':
            
            result_gaussian = ndimage.gaussian_filter(masked_input, sigma=sig)
            
            if str(AnalysisGui.thresholdmethod.currentIndex()) == '0':
                
                ret_log, thresh_log = cv2.threshold(result_gaussian,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            
            elif str(AnalysisGui.thresholdmethod.currentIndex()) == '1':
                
                manual_threshold = AnalysisGui.ThresholdSlider.value()*2.55
                
                ret_log, thresh_log = cv2.threshold(result_gaussian,0,255,cv2.THRESH_BINARY_INV+manual_threshold)
            
            bin_img_g = (1-thresh_g/255).astype('bool')
            spots_img_g = (bin_img_g*255).astype('uint8')
            kernel = np.ones((3,3), np.uint8)
            spot_openned_g = cv2.morphologyEx(spots_img_g, cv2.MORPH_OPEN, kernel)
            final_spots = spot_openned_g
        
        ### center of mass calculation
        if str(AnalysisGui.SpotLocationCbox.currentIndex()) == '0':
            
            labeled_spots, num_features = label(final_spots)
            spot_labels = np.unique(labeled_spots)
            
            bin_img = (final_spots/uint8_max_val).astype('bool')
            ## Binary image filling
            masked_spots = np.multiply(masked_input,bin_img)
            
            spot_locations = ndimage.measurements.center_of_mass(masked_spots, labeled_spots, spot_labels[spot_labels>0])
            
            ###### Brightest spot calculation
        if str(AnalysisGui.SpotLocationCbox.currentIndex()) == '1':
            
            labeled_spots, num_features = label(final_spots)
            spot_labels = np.unique(labeled_spots)
            bin_img = (final_spots/uint8_max_val).astype('bool')
            masked_spots = np.multiply(masked_input,bin_img)
            spot_locations = peak_local_max(masked_spots, labels=labeled_spots, num_peaks_per_label=1)
        
            ##### Centroid calculation
        if str(AnalysisGui.SpotLocationCbox.currentIndex()) == '2':
            
            labeled_spots, num_features = label(final_spots)
            spot_labels = np.unique(labeled_spots)
            
            spot_locations = ndimage.measurements.center_of_mass(final_spots, labeled_spots, spot_labels[spot_labels>0])
                        
        return spot_locations
    
    def COORDINATES_TO_CIRCLE(self, coordinates,ImageForSpots):
        
        circles = np.zeros((ImageForSpots.shape), dtype=np.uint8)
        for center_y, center_x in zip(coordinates[:,0], coordinates[:,1]):
                circy, circx = circle_perimeter(center_y, center_x, 7, shape=ImageForSpots.shape)
                circles[circy, circx] = 255


        return circles
    
    