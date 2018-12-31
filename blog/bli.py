def BL_interp_1D(x, z, T, order, grid_step=0.01, win=True):
    """
    Band-limited interpolation of 1D functions (P.Prandoni, M.Vetterli)
    """
    # Create Fourier order vector
    k = expand_dims(arange(-order, order+1), 0)
    
    # construct the Fourier matrix
    F = exp(2j*pi*x*k/(T[1]-T[0]))
    
    # Least-square projection (alternatively linalg.lstsq can be used)
    C = dot(dot(linalg.inv(dot(F.T,F)), F.T), z)
    
    # create new evenly spaced grid
    xg = expand_dims(arange(T[0], T[1], grid_step), 1)
    
    # window the Fourier coefficients if requested
    if (win):
        C *= expand_dims(hanning(2*order+1), 1)
    
    zg = dot(exp(2j*pi*xg*k/(T[1]-T[0])), C)
        
    return zg, xg, C, k
