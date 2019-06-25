using System;
using Client.ServiceReference1;
using Newtonsoft.Json.Linq;
using Client.models;
using Client.exceptions;
using System.Collections.Generic;
namespace Client

{
  class GetRecommendationCommand : ACommand
  {

    public GetRecommendationCommand()
    {
      name = "getrec";
      description = "get recipe recommendations for the given users";
      parameters = "<user_1> <user_2> ... <user_n>";
      nb_parameters = 1;
      options = new List<Option>();
      options.Add(new Option("-f" ,"take the fridge into account"));
    }
    public GetRecommendationCommand(String[] args, String [] options) : this()
    {

      base.args = args;
      activated_options = options;


    }
    protected override Boolean run()
    {

      if (!checkArgs(args))
      {
        throw new InvalidParametersException("Invalid parameters, you must provide integers", ToString());
      }
      Console.WriteLine("Getting recommendations...");
      IService1 service = new Service1Client();
      JArray array = JArray.Parse(service.getRecommendations(args));
      foreach(JObject x in array )
      {
        displayRecipe(x);

      }

      return false;
    }

    protected override Boolean fixedParameters()
    {
      return false;
    }

    private void displayRecipe(JObject j)
    {
      Console.WriteLine("\n");
      Console.WriteLine("==============================================================================================================");
      Console.WriteLine("Recipe n° " + j["RecipeID"] + " : " + j["Recipe Name"]);
      Console.WriteLine("==============================================================================================================");
      Console.WriteLine("Ingredients : " + j["Ingredients"]);
      Console.WriteLine("Directions : " + j["Directions"]);
      Console.WriteLine("Cook Time : " + j["Cook Time"]);
      Console.WriteLine("Prepare Time : " + j["Prepare Time"]);
      Console.WriteLine("Total Time : " + j["Total Time"]);
      Console.WriteLine("Reviews Count : " + j["Review Count"]);
      Console.WriteLine("\n");
    }

    private Boolean checkArgs(String[] args)
    {
      foreach(var s in args)
      {
        int myInt;
        if(!int.TryParse(s, out myInt))
        {
          return false;
        }
      }
      return true;
    }

    protected override bool hasOptions()
    {
      return true;
    }

  }
}
