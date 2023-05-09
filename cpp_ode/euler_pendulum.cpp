#include <iostream>
#include <cmath>

using namespace std;

double dwdt(double theta) {

  double L, g;

  g = 9.81;
  L = 10;

  return  -g/L * sin(theta);
};

int main () {

  double theta, w, dt, t, tmax;
  double dtheta, dw;

  t = 0;
  tmax = 20;
  dt = 0.001;
  theta = 1.75;
  w = 0;

  do {

    cout << t << " " << theta << endl;
    
    dtheta = w;
    dw = dwdt(theta);

    theta = theta + dt*dtheta;
    w = w + dt*dw;


    t += dt;

  } while (t <= tmax);

  return 0;
  
}
