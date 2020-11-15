#Código apenas em mockup desenvolvido na alexa developer console

# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Olá, Como posso te ajudar?. Lembre que a qualquer momento pode falar ajuda e eu te digo as opções"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class AcaoIntentHandler(AbstractRequestHandler):
    #identificar qual a ação que queremos fazer
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AcaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slot = ask_utils.request_util.get_slot(handler_input, "slAcao")
        #if slot.value=='Bolsa de Valores':
        #    speak_output = "Claro!, o que você gostaria de saber"
        #else:
        #    speak_output="não entendi, pode repetir"
        #speak_output = "Claro!, o que você gostaria de saber?"
        #speak_output= slot.value
        
        return (
            handler_input.response_builder
               
                        #speak_output = "Claro!, o que você gostaria de saber?"
                .speak(speak_output)
                .ask(speak_output)
                .response
    )

class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent.""" 
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Olá mundo!"
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class OutroTesteIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("OutroTesteIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "De qual ação gostaria de informação?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
class SaldoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_intent_name("SaldoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Enviei uma mensagem para o seu celular com uma senha para confirmar se posso dizer o saldo em voz alta. Pode me informar a senha recebida?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
    
class AgendaAplicacaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AgendaAplicacaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Enviei uma mensagem para o seu celular com uma senha de confirmação . Pode me informar a senha recebida?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CompraAtivoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CompraAtivoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Sua solicitação foi realizada com sucesso. Enviei um e-mail para você com os detalhes da transação"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class SenhasaldoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SenhasaldoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Seu Saldo é de R$2000,00"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class SenhaAgendaIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SenhaAgendaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Sua solicitação foi realizada com sucesso. Enviei um e-mail para você com os detalhes da transação"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
class RentabilidadeAcaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RentabilidadeAcaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "A Petrobras teve um oscilação positiva de 25% nos últimos 6 meses"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class ValorAcaoIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ValorAcaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "O valor da ação PETR4 fechou em R$ 21,91 em 12 de novembro de 2020."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class RentabilidadeCarteiraIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RentabilidadeCarteiraIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Sua carteira teve uma oscilação positiva de 0,8% nos últimos 30 dias"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
        
class M_CallIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("M_CallIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = """ 
Ontem o ibovespa sustentou os cem mil pontos pela maior parte do pregão, mas perdeu a força na reta final dos negócios; esse comportamento também se repetiu no mercado americano.
A correção dos índices ocorreu em meio ao aumento da preocupação quanto a volta das restrições as atividades dos Estados Unidos, a califórnia por exemplo determinou o fechamento dos estabelecimentos como bares e restaurantes devido a covid dezenove, antes disso, na primeira metade da sessão os ganhos aqui chegavam perto de um porcento; contribuiu mais uma vez para o bom humor, o noticiário das vacinas sobre o corona vírus em desenvolvimento, a americana fáizer e a alemã Laion tec anunciaram ontem que duas de suas vacinas experimentais receberam o istátus de fast track da agência reguladora de medicamentos dos Estados Unidos; o que acelera o processo de revisão e aprovação da substância.
Se os atuais testes forem bem sucedidos os testes devem iniciar ainda em Julho; elas afirmam que se forem bem sucedidas poderão produzir até cem milhões de doses já nesse ano e mais de um bilhão durante o ano que vem.
Por aqui no Brasil o tesouro nacional informou que repassou ontem quinze bilhões de reais a estados e municípios, foi a segunda parcela do socorro aprovado para recompor parte da receita dos entes corporativos diante da crise causada pela pandemia, o valor também será pago em agosto e setembro totalizando um auxílio de sessenta bilhões de reais.
Na segunda feira o IBOVESPA caiu 1,33% e fechou aos noventa e oito mil seissentos e noventa e sete pontos, já o dólar comercial encerrou o dia em alta de 1,28% cotado a cinco reais e trinta e oito centavos.
Hoje o Banco central irá divulgar o PIB do país, depois de recuar 9,7% em abril o IBCBR deverá mostrar alta de 7,2% em maio segundo os cálculos da equipe de macroeconomia do banco safra, em relação a maio do ano passado o índice deve apresentar uma retração 11%.
Estamos ainda monitorando a agenda de concessões no país; o ministério de minas e energia divulgou ontem uns cinco leilões para novos projetos de transição; com a redução da demanda de energia por conta da crise haverá um único leilão esse ano em dezembro, o governo pretende licitar com ele mais de seis bilhões de reais em investimentos, em outra frente a agência nacional de transportes terrestres enviou ao TCU o projeto de concessão da ferro grão , ferrovia com mais de novecentos quilômetros de extensão que ligará Sinope no Mato Grosso a Itaítuba no Pará, a análise pelo tribunal é a última etapa para a publicação do edital que deverá gerar investimentos de quase oito bilhões e meio de reais segundo o governo, estes foram os principais destaques desse morning call desta terça feira. Ótimo dia e bons negócios.
        """
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AcaoIntentHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(OutroTesteIntentHandler())
sb.add_request_handler(SaldoIntentHandler())
sb.add_request_handler(AgendaAplicacaoIntentHandler())
sb.add_request_handler(CompraAtivoIntentHandler())
sb.add_request_handler(SenhaAgendaIntentHandler())
sb.add_request_handler(SenhasaldoIntentHandler())
sb.add_request_handler(RentabilidadeAcaoIntentHandler())
sb.add_request_handler(ValorAcaoIntentHandler())
sb.add_request_handler(RentabilidadeCarteiraIntentHandler())
sb.add_request_handler(M_CallIntentHandler())

lambda_handler = sb.lambda_handler()
