import math

def solve():
    W, H, X, Y, R, Vx, Vy, A = map(float, input().split())
    dt = 0.01  # Time step
    
    while True:
        V = math.sqrt(Vx*Vx + Vy*Vy)
        if V < 0.0001: # Stop if velocity becomes too small
            break
        
        X += Vx * dt
        Y += Vy * dt
        
        # Bouncing off the walls
        if Y < R:
            Y = R + (R-Y)
            Vy *= -1
        elif Y > H - R:
            Y = H-R - (Y-(H-R))
            Vy *= -1
        if X < R:
            X = R + (R - X)
            Vx *= -1
        elif X > W - R:
            X = W - R - (X - (W - R))
            Vx *= -1
        
        # Slowing down
        V -= A * dt
        
        if V < 0:
          V = 0
        
        angle = math.atan2(Vy, Vx)
        Vx = V * math.cos(angle)
        Vy = V * math.sin(angle)
    
    print(round(X), round(Y))

if __name__ == "__main__":
    solve()