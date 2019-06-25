using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client.exceptions
{
  class CommandUnknowknException : Exception
  {
    public CommandUnknowknException() : base("The command is unknowkn, to see the commands availbalbe, type '?")
    {}
  }
}
