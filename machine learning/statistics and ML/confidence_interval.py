    """ Confidence interval - Estimate a populational parameter: MEAN: ------------------------------------ ####"""
    from scipy.stats import sem, t, norm
    from scipy import mean
    import math
    
    
    def confidence_interval(data, confidence):
    
        #sample size (n)
        n = len(data)
        
        #sample mean (X|)
        m = mean(data)    
        
        #sample standard deviation (s)
        std_err = sem(data)
        
        #Gauss Z ----------------------------
        if  n > 30:
            h = (norm.ppf((1 + confidence) / 2, n) ) * std_err  /  math.sqrt(n)
            test_stat = stats.norm.ppf((interval + 1)/2)
        
                
        #Student's T ------------------------
        """n > 30 (Gauss, Z): 
        CI(Mean) = sample_mean +- (Z (confidence_level/2) * sample_std/ sqrt(sample_n)) """
        else:
            
            #calculate T
            #in portuguese, we call g.l (graus de liberdade)
            degrees_of_freedom = n - 1
            """
            #n <= 30 (Student's T): 
            The same thing above. The only difference is that we change Z for T
                CI(Mean) = sample_mean +- (T (confidence_level/2) * sample_std/ sqrt(sample_n))"""
            
            h = (t.ppf((1 + confidence) / 2, degrees_of_freedom) ) * std_err  /  math.sqrt(n)
        
        
        #start of interval
        start = m - h
        print(start)
        
        #end of interval
        end = m + h
        print(end)
        
        print("the interval is between %.3f and %.3f"% (start, end))
        
    
    #------------------------------------------------------------------------------------------#############    
    confidence = 0.95
    data = [1, 2, 3, 4, 5]
    
    confidence_interval(data, confidence)