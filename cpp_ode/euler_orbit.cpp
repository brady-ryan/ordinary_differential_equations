#include <iostream>
#include <cmath>

using namespace std;


double dudt(double x, double y) {

  double GM;
  double r;

  GM = -39.47;
  r = sqrt(pow(x,2) + pow(y,2));

  return (GM*x)/pow(r,3);
};

double dvdt(double x, double y) {

  double GM;
  double r;

  GM = -39.47;
  r = sqrt(pow(x,2) + pow(y,2));

  return (GM*y)/pow(r,3);
};

int main () {

  double x, y, u, v;
  double t, tmax, dt;
  double du, dv;
  double PI;

  PI = 3.14159;

  t = 0;
  tmax = 1.0;
  dt = 0.001;
  x = 0;
  y = 1;
  u = 2*PI;
  v = 0;


  do {

    cout << x << " " << y << endl;

    du = dudt(x,y);
    dv = dvdt(x,y);

    
    u = u + dt*du;
    v = v + dt*dv;
    x = x + dt*u;
    y = y + dt*v;
    t += dt;

  } while (t <= tmax);

  return 0;
}
