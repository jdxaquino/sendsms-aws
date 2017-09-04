// Importamos la Biblioteca GSM
//0: GSM Conectado
//#: Ingreso de Numero
//@: Ingreso de Mensaje
//1: Confirmacion Envio del Mensaje
#include <GSM.h>

#define PINNUMBER ""

// Instanciamos la Libreria
GSM gsmAccess;
GSM_SMS sms;

void setup()
{
  // Inicializando la comunicacion mientras esperamos que el abra el puerto:
  Serial.begin(9600);  
  //Serial.println("Envio de Mensajes SMS");

  // Verificando Estado de Conexion
  boolean notConnected = true;

  // Comienza a ejecutar Placa GSM
  // Utiliza el PIN como argumento y mensaje de modem conectado a la Placa GSM
  while(notConnected)
  {
    if(gsmAccess.begin(PINNUMBER)==GSM_READY)
      notConnected = false;
    else
    {
      Serial.println("9");
      delay(1000);
    }
  }  
  Serial.print("0\n");//ok
}

void loop()
{
  // Almacenaje de tu Telefono Celular
  //Serial.print("#\n");
  char command[20];
  char phone_number[20];
  char message[200];
  readSerial(command); 
  if (command[0] == '*'){
    readSerial(phone_number); 
    //Serial.print("#\n");//ok  
    readSerial(message);
    //Serial.print("@\n");//ok  
    sms.beginSMS(phone_number);
    sms.print(message);
    sms.endSMS(); 
    Serial.print("1\n");
  } 
}

int readSerial(char result[])
{
  int i = 0;
  while(1)
  {
    while (Serial.available() > 0)
    {
      char inChar = Serial.read();
      if (inChar == '\n')
      {
        result[i] = '\0';
        Serial.flush();
        return 0;
      }
      if(inChar!='\r')
      {
        result[i] = inChar;
        i++;
      }
    }
  }
}

