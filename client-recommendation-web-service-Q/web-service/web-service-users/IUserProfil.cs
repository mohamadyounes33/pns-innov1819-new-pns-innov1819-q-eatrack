using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;


namespace web_service_users
{
  // REMARQUE : vous pouvez utiliser la commande Renommer du menu Refactoriser pour changer le nom d'interface "IService1" à la fois dans le code et le fichier de configuration.
  [ServiceContract]
  public interface IUserProfil
  {
    [OperationContract]
    string addToFridge(string[] args);
    [OperationContract]
    string removeFromFridge(string[] args);
    [OperationContract]
    string inquirePreferences(string[] args);
    [OperationContract]
    string removePreferences(string[] args);
    [OperationContract]
    string inquireAllergies(string[] args);
    [OperationContract]
    string removeAllergies(string[] args);
    [OperationContract]
    string emptyFridge(string[] args);

    // TODO: ajoutez vos opérations de service ici
  }

  // Utilisez un contrat de données comme indiqué dans l'exemple ci-après pour ajouter les types composites aux opérations de service.
  // Vous pouvez ajouter des fichiers XSD au projet. Une fois le projet généré, vous pouvez utiliser directement les types de données qui y sont définis, avec l'espace de noms "web_service_users.ContractType".
  [DataContract]
  public class CompositeType
  {
    bool boolValue = true;
    string stringValue = "Hello ";

    [DataMember]
    public bool BoolValue
    {
      get { return boolValue; }
      set { boolValue = value; }
    }

    [DataMember]
    public string StringValue
    {
      get { return stringValue; }
      set { stringValue = value; }
    }
  }
}
