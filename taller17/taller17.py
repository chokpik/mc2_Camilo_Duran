import math

def main():
    x = [1.2,2.4,3.6,4.8,6,7] #0
    y = [0.8,1,1.5,2,2.9,3.6] #1
    lnY = [0 for i in range(len(y))]

    #Crear lista de lnY
    for i in range(len(y)):
        lnY[i] = math.log(y[i])
    
    A = [x,lnY]
    n = len(A[0])
    sumX = 0.0
    sumlnY = 0.0
    sumXlnY = 0
    sumX2 = 0.0

    for i in range(n):
        
        sumX += A[0][i]
        sumlnY += A[1][i]
        sumXlnY += (A[0][i]*A[1][i])
        sumX2 += (A[0][i]*A[0][i])
    
    promX = sumX/n
    promlnY = sumlnY/n
    
    #formulita
    a1 = (n*sumXlnY-sumX*sumlnY)/(n*sumX2-pow(sumX,2))
    a0 = promlnY - a1*promX

    #alpha
    alpha = math.exp(a0)

    print(f"respuesta :y = {alpha}*e^{a1}x")



if __name__ == '__main__':
    main()