real function dwdt(theta)
  implicit none

  real :: g = 9.81, L = 10, theta

  dwdt = -g/L * sin(theta)
end function dwdt


program pendulum
  implicit none

  real :: theta = 1.75, w = 0
  real :: dtheta, dw
  real :: dwdt
  real :: theta_new, w_new
  real :: t = 0, tmax = 20, dt = 0.01

  do while (t < tmax)

     theta_new = theta + dt*w

     dw = dwdt(theta)

     w_new = w + dt*dw

     theta = theta_new
     w = w_new

     print *, t, theta

     t = t+dt

  end do

  stop 0

end program pendulum


     
