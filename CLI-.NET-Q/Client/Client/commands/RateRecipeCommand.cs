using System;
using Client.exceptions;
using Client.ServiceReference1;
using System.Collections.Generic;
using Client.models;


namespace Client
{
  class RateRecipeCommand : ACommand
  {

    public RateRecipeCommand()
    {
      name = "raterecipe";
      parameters = "<userID> <recipeID> <rating>";
      description = "give a rating from 0 to 5";
      nb_parameters = 3;
      options = new List<Option>();

    }

    public RateRecipeCommand(String[] args, String[] options) : this()
    {
      base.args = args;
      activated_options = options;

    }
    protected override Boolean run()
    {
      if (!checkArgs(args))
      {
        throw new InvalidParametersException("You must provide integers, the second must be between 0 and 5", ToString());
      }
      Console.WriteLine("Your rating is being submited...");
      System.Threading.Thread.Sleep(1000);
      Console.WriteLine("Thank you for your feedback :)");
      IService1 service = new Service1Client();
      Console.WriteLine(service.evaluateRecipe(args));
  
      return false;

    }

    private Boolean checkArgs(string[] args)
    {
      foreach (var s in args)
      {
        int myInt;
        if (!int.TryParse(s, out myInt))
        {
          return false;
        }
      }
      var c2 = int.Parse(args[2]);
      if(c2 < 0 || c2 > 5)
      {
        return false;
      }
      return true;
    }


  }
}
