using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client.exceptions
{
  class MissingParametersException : Exception
  {
    public MissingParametersException(String[] args, int nb_parameters, String correction, Boolean fixedParameters) :base("You entered " + args.Length + " parameters but this command requires " + (fixedParameters? "" :"at least ") + nb_parameters + "\n The correct usage is : \n" + correction)
      {}
  }
}
