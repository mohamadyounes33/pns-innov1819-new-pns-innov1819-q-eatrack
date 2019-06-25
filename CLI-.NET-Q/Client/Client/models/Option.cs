using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Client.models
{
  class Option
  {

    private String name;
    private String description;

    public Option(string name, string description)
    {
      this.name = name;
      this.description = description;
    }

    public override string ToString()
    {
      return name + " : " + description;
    }

    public string getName()
    {
      return name;
    }

  }
}
