real function dvxdt(x, y)
  implicit none

  real :: GM = 39.47, r, x, y

  r = sqrt(x**2 + y**2)

  dvxdt = (-GM*x)/r**3
end function dvxdt

real function dvydt(x, y)
  implicit none

  real :: GM = 39.47, r, x, y

  r = sqrt(x**2 + y**2)

  dvydt = (-GM*y)/r**3
end function dvydt

program euler
  implicit none

  real, parameter :: GM = 1, PI = 3.14159
  real :: t = 0, tmax = 1, dt = 0.01
  real :: x = 0, y = 1, vx = 2*PI, vy = 0
  real :: xnew, ynew, vxnew, vynew
  real, external :: dvxdt, dvydt
  integer :: openfile

  open(newunit = openfile, file = 'data.dat', status = 'REPLACE')

  do while (t < tmax)

    xnew = x + dt*vx
    ynew = y + dt*vy

    vxnew = vx + dt*dvxdt(xnew, ynew)
    vynew = vy + dt*dvydt(xnew, ynew)

    x = xnew
    y = ynew
    vx = vxnew
    vy = vynew

    write(openfile,*) x, y

    t = t + dt
 end do

 close(unit = openfile)
 
 stop 0
 
end program euler
