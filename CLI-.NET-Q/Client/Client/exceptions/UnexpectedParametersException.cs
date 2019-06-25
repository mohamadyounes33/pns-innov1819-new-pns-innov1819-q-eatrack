using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client.exceptions
{
  class UnexpectedParametersException: Exception
  {
    public UnexpectedParametersException(string[] args, int nb_parameters, string correction, Boolean fixedParameters) : base("You entered " + args.Length + " parameters but this command requires " + (fixedParameters ? "" : "at most ") + nb_parameters + "\n The correct usage is : \n" + correction)
    { }
  }
}
