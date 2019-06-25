using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client.exceptions
{
  class InvalidParametersException : Exception

  {
    public InvalidParametersException(string message, string correction) : base(message + "\n" + "The correct usage is\n " + correction) { }
  }
}
