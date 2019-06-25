using System;
using Client.exceptions;
using System.Collections.Generic;
using Client.models;
using System.Linq;

namespace Client
{
  abstract class ACommand

  {
    protected String name;
    protected String description;
    protected string parameters;
    protected int nb_parameters;
    protected String[] args;
    protected List<Option> options;
    protected string[] activated_options;

    public string getName()
    {
      return name;
    }

    public string getDescription()
    {
      return description;
    }

    public string getParameters()
    {
      return parameters;
    }

    public override string ToString()
    {
      string command = "- " + name + (parameters == null ? "" : " ") + parameters + " : " + description;
      string options = hasOptions() ? "\n**Options** :\n":"";
      foreach(Option c in this.options)
      {
        options += "\t*" + c + "\n";
      }
      return command + options;

    }
    public Boolean execute()
    {


      if (args.Length < nb_parameters )
      {

        throw new MissingParametersException(args, nb_parameters, ToString(), fixedParameters());
      }

      if (args.Length > nb_parameters && fixedParameters())
      {
        throw new UnexpectedParametersException(args, nb_parameters, ToString(), fixedParameters());
      }
      if (!checkOptions())
      {
        throw new Exception("Some of the options you entered does not exist for this command");
      }

        
      
      return run();

    }

    protected abstract Boolean run();

    protected  virtual Boolean fixedParameters()
    {
      return true;
    }

    protected virtual Boolean hasOptions()
    {
      return false;
    }

    private Boolean checkOptions()
    {
      String[] options_names = options.Select(x => x.getName()).ToArray();
      foreach (String s in activated_options)
      {
        if (!options_names.Contains(s))
        {
          return false;
        }
      }
      return true;
    }

  }
}
