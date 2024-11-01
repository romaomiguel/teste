import pywhatkit as kit
from datetime import datetime, timedelta

def test_send_whatsapp():
    product_name = "Produto Teste"
    expiry_date = "2024-11-05"
    phone_number = "+5565999161641"  # seu número

    # Enviar mensagem no próximo minuto
    agora = datetime.now()
    envio_hora = agora + timedelta(minutes=1)
    hora = envio_hora.hour
    minuto = envio_hora.minute

    try:
        kit.sendwhatmsg(phone_number, f"Aviso: O produto '{product_name}' está com validade próxima ({expiry_date})", hora, minuto)
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")

if __name__ == "__main__":
    test_send_whatsapp()
