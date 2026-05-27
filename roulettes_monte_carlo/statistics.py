# statistics.py
import math

def get_mean_and_std(data):
    """
    Calculates the sample mean and the standard deviation of a dataset.
    
    Mathematical Formulas Applied:
    Mean (mu) = sum(x) / N
    Variance = sum((x - mu)^2) / N
    Standard Deviation (sigma) = sqrt(Variance)
    """
    if not data:
        return 0.0, 0.0
        
    n = len(data)
    mean = sum(data) / n
    
    variance = sum([(x - mean) ** 2 for x in data]) / n
    std_deviation = math.sqrt(variance)
    
    return mean, std_deviation


def get_confidence_margin(std_deviation, confidence_level=0.95):
    """
    Calculates the margin of error using the Empirical Rule for a normal distribution.
    For a 95% confidence interval, the critical Z-score value is approximately 1.96.
    """
    if confidence_level == 0.95:
        z_score = 1.96
    else:
        z_score = 1.96
        
    return std_deviation * z_score