def convolve(im, k):
    im = im.astype(np.float64)
    k = k.astype(np.float64)
    rows = im.shape[0]
    cols = im.shape[1]
    k_r = k.shape[0]
    k_c = k.shape[1]
    res = np.zeros(im.shape)
    for i in range(int(k_r/2), rows - int((k_r-1) / 2)):
        for j in range(int(k_c/2), cols - int((k_c - 1) / 2)):
            l_r = i - int(k_r / 2)
            r_r = i + int((k_r - 1) / 2)
            l_c = j - int(k_c / 2)
            r_c = j + int((k_c - 1) / 2)
            res[i][j] = max(0, sum(sum(k * im[l_r : r_r + 1, l_c : r_c + 1])))
    return res.astype(np.int)


def bilateral_filter_inefficient(img, sigma_d, sigma_r, sz):
    #gaussian_kernel = 
    #for i in range(sz):
    #    for j in range(sz):
            
    img = img.astype(np.float64)
    row = img.shape[0]
    col = img.shape[1]
    res = np.zeros(img.shape)
    for i in range(int(sz / 2), row - int(sz / 2)):
        for j in range(int(sz / 2), col - int(sz / 2)):
            for c in range(3):
                s = 0
                for k in range(i - int(sz / 2), i + int(sz / 2) + 1):
                    for l in range(j - int(sz / 2), j + int(sz / 2) + 1):
                        ttt = np.exp(-((i - k) * (i - k) + (j - l) * (j - l)) / (2 * sigma_d * sigma_d)) * np.exp(-((img[i][j][c] - img[k][l][c]) * (img[i][j][c] - img[k][l][c])) / (2 * sigma_r * sigma_r))
                        s = s + ttt
                        res[i][j][c] = res[i][j][c] + img[k][l][c] * ttt
                res[i][j][c] = res[i][j][c] / s
    return res.astype(np.uint8)