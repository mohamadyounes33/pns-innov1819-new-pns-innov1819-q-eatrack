using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Client.ServiceReference1;

namespace Client
{
  class Recommender
  {
    IService1 service1 = new Service1Client();
  }
}
