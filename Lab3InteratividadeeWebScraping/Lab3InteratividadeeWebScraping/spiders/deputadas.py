from wsgiref import headers
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
import scrapy
import pandas as pd




class DeputadosSpider(scrapy.Spider):
    name = "deputadas"

    def start_requests(self):
        urls = ['https://www.camara.leg.br/deputados/204528',
                'https://www.camara.leg.br/deputados/204545',
                'https://www.camara.leg.br/deputados/74057',
                'https://www.camara.leg.br/deputados/204353',
                'https://www.camara.leg.br/deputados/204400',
                'https://www.camara.leg.br/deputados/73696',
                'https://www.camara.leg.br/deputados/123756',
                'https://www.camara.leg.br/deputados/204509',
                'https://www.camara.leg.br/deputados/73701',
                'https://www.camara.leg.br/deputados/207176',
                'https://www.camara.leg.br/deputados/204374',
                'https://www.camara.leg.br/deputados/160589',
                'https://www.camara.leg.br/deputados/213762',
                'https://www.camara.leg.br/deputados/204507',
                'https://www.camara.leg.br/deputados/164360',
                'https://www.camara.leg.br/deputados/204369',
                'https://www.camara.leg.br/deputados/204380',
                'https://www.camara.leg.br/deputados/204462',
                'https://www.camara.leg.br/deputados/178928',
                'https://www.camara.leg.br/deputados/178939',
                'https://www.camara.leg.br/deputados/204459',
                'https://www.camara.leg.br/deputados/81297',
                'https://www.camara.leg.br/deputados/204434',
                'https://www.camara.leg.br/deputados/178994',
                'https://www.camara.leg.br/deputados/204421',
                'https://www.camara.leg.br/deputados/74075',
                'https://www.camara.leg.br/deputados/220008',
                'https://www.camara.leg.br/deputados/218086',
                'https://www.camara.leg.br/deputados/160575',
                'https://www.camara.leg.br/deputados/204407',
                'https://www.camara.leg.br/deputados/204354',
                'https://www.camara.leg.br/deputados/160598',
                'https://www.camara.leg.br/deputados/204447',
                'https://www.camara.leg.br/deputados/178966',
                'https://www.camara.leg.br/deputados/107283',
                'https://www.camara.leg.br/deputados/129618',
                'https://www.camara.leg.br/deputados/198197',
                'https://www.camara.leg.br/deputados/67138',
                'https://www.camara.leg.br/deputados/74848',
                'https://www.camara.leg.br/deputados/108338',
                'https://www.camara.leg.br/deputados/178839',
                'https://www.camara.leg.br/deputados/204468',
                'https://www.camara.leg.br/deputados/204546',
                'https://www.camara.leg.br/deputados/74856',
                'https://www.camara.leg.br/deputados/160534',
                'https://www.camara.leg.br/deputados/178832',
                'https://www.camara.leg.br/deputados/204375',
                'https://www.camara.leg.br/deputados/139285',
                'https://www.camara.leg.br/deputados/204405',
                'https://www.camara.leg.br/deputados/204410',
                'https://www.camara.leg.br/deputados/74784',
                'https://www.camara.leg.br/deputados/178866',
                'https://www.camara.leg.br/deputados/166402',
                'https://www.camara.leg.br/deputados/204458',
                'https://www.camara.leg.br/deputados/204471',
                'https://www.camara.leg.br/deputados/204430',
                'https://www.camara.leg.br/deputados/171619',
                'https://www.camara.leg.br/deputados/74398',
                'https://www.camara.leg.br/deputados/204540',
                'https://www.camara.leg.br/deputados/178956',
                'https://www.camara.leg.br/deputados/204428',
                'https://www.camara.leg.br/deputados/204432',
                'https://www.camara.leg.br/deputados/204453',
                'https://www.camara.leg.br/deputados/66179',
                'https://www.camara.leg.br/deputados/216198',
                'https://www.camara.leg.br/deputados/205535',
                'https://www.camara.leg.br/deputados/204377',
                'https://www.camara.leg.br/deputados/73943',
                'https://www.camara.leg.br/deputados/204529',
                'https://www.camara.leg.br/deputados/204565',
                'https://www.camara.leg.br/deputados/160639',
                'https://www.camara.leg.br/deputados/160641',
                'https://www.camara.leg.br/deputados/204467',
                'https://www.camara.leg.br/deputados/215361',
                'https://www.camara.leg.br/deputados/178925',
                'https://www.camara.leg.br/deputados/178989',
                'https://www.camara.leg.br/deputados/204525',
                'https://www.camara.leg.br/deputados/178945',
                'https://www.camara.leg.br/deputados/204357',
                'https://www.camara.leg.br/deputados/204535',
                'https://www.camara.leg.br/deputados/178961',
                'https://www.camara.leg.br/deputados/204360',
                'https://www.camara.leg.br/deputados/178946',
                'https://www.camara.leg.br/deputados/204534',
                'https://www.camara.leg.br/deputados/204464',
                'https://www.camara.leg.br/deputados/178901',
                'https://www.camara.leg.br/deputados/204466',
                'https://www.camara.leg.br/deputados/178862',
                'https://www.camara.leg.br/deputados/215044'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        nome = response.css("ul.informacoes-deputado").getall()
        nome_deputada = Selector(text=nome[0]).xpath('//li/text()').get()

        presenca_ple = response.css("ul.list-table__content").getall()
        presenca_plenario = int(Selector(text=presenca_ple[0]).xpath('//dd/text()').get().strip().split()[0])
        ausencia_jus_plenario = response.css(".list-table__item:nth-child(1) .list-table__definition-description:nth-child(4)").getall()
        ausencia_n_jus_plenario = response.css(".list-table__item:nth-child(1) .list-table__definition-description:nth-child(6)").getall()

        ausencia_justificada_plenario = int(Selector(text=ausencia_jus_plenario[0]).xpath('//dd/text()').get().strip().split()[0])
        ausencia_nao_justificada_plenario = int(Selector(text=ausencia_n_jus_plenario[0]).xpath('//dd/text()').get().strip().split()[0])
        ausencia_plenario = ausencia_justificada_plenario + ausencia_nao_justificada_plenario

        presenca_com = response.css(".list-table__item+ .list-table__item .list-table__definition-description:nth-child(2)").getall()
        ausencia_jus_com = response.css(".list-table__item+ .list-table__item .list-table__definition-description:nth-child(4)").getall()
        ausencia_n_jus_com = response.css(".list-table__item+ .list-table__item .list-table__definition-description:nth-child(6)").getall()

        presenca_comissao = int(Selector(text=presenca_com[0]).xpath('//dd/text()').get().strip().split()[0])
        ausencia_justificada_comissao =int(Selector(text=ausencia_jus_com[0]).xpath('//dd/text()').get().strip().split()[0])
        ausencia_nao_justificada_comissao =int(Selector(text=ausencia_n_jus_com[0]).xpath('//dd/text()').get().strip().split()[0])
        ausencia_comissao = ausencia_justificada_comissao + ausencia_nao_justificada_comissao

        data_nasc = response.css("#identificacao li:nth-child(5)").getall()
        data_nascimento = Selector(text=data_nasc[0]).xpath('//li/text()').get().strip()
        
        gasto_par_mensal = response.css("table#gastomensalcotaparlamentar").getall()
        gasto_t_par = response.css("table#percentualgastocotaparlamentar").getall()
        gasto_total_par = float(Selector(text = gasto_t_par[0]).xpath('//tr[1]//td[2]//text()').extract_first().replace('.','').replace(',','.'))

        gasto_jan_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[1]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_fev_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[2]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_mar_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[3]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_abr_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[4]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_maio_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[5]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_junho_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[6]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_jul_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[7]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_agosto_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[8]//td[2]//text()').extract_first().replace('.','').replace(',','.')) 
        gasto_set_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[9]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_out_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[10]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_nov_par = float(Selector(text = gasto_par_mensal[0]).xpath('//tr[11]//td[2]//text()').extract_first().replace('.','').replace(',','.')) 

        salario_b = response.css("li:nth-child(2) .beneficio__info").getall()
        salario_bruto_par = float(Selector(text=salario_b[0]).xpath('//a/text()').get().strip().split()[1].replace('.','').replace(',','.')) 

        gasto_gab_mensal = response.css("table#gastomensalverbagabinete").getall()
        gasto_t_gab = response.css("table#percentualgastoverbagabinete").getall()
        gasto_total_gab = float(Selector(text = gasto_t_gab[0]).xpath('//tr[1]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_jan_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[1]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_fev_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[2]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_mar_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[3]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_abr_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[4]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_maio_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[5]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_junho_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[6]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_jul_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[7]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_agosto_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[8]//td[2]//text()').extract_first().replace('.','').replace(',','.')) 
        gasto_set_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[9]//td[2]//text()').extract_first().replace('.','').replace(',','.'))
        gasto_out_gab = float(Selector(text = gasto_gab_mensal[0]).xpath('//tr[10]//td[2]//text()').extract_first().replace('.','').replace(',','.'))

        viagem = response.css(".beneficio__viagens .beneficio__info").getall()
        quant_viagem  = int(Selector(text=viagem[0]).xpath('//span/text()').get().strip()) 

         

        lista_deputadas ={
          'nome':nome_deputada,
          'genero':"F",
          'presenca_plenario':presenca_plenario,
          'ausencia_plenario':ausencia_plenario,
          'ausencia_justificada_plenario':ausencia_justificada_plenario,
          'presenca_comissao': presenca_comissao,
          'ausencia_comissao' : ausencia_comissao,
          'ausencia_justificada_comissao' : ausencia_justificada_comissao,
          'data_nascimento' : data_nascimento,
          'gasto_total_par': gasto_total_par,
          'gasto_jan_par': gasto_jan_par,
          'gasto_fev_par': gasto_fev_par,
          'gasto_mar_par': gasto_mar_par,
          'gasto_abr_par': gasto_abr_par,
          'gasto_maio_par': gasto_maio_par,
          'gasto_junho_par' : gasto_junho_par,
          'gasto_jul_par' : gasto_jul_par, 
          'gasto_agosto_par' : gasto_agosto_par,
          'gasto_set_par' : gasto_set_par,
          'gasto_out_par' : gasto_out_par,
          'gasto_nov_par ' : gasto_nov_par,
          'salario_bruto_par' : salario_bruto_par,
          'gasto_total_gab' : gasto_total_gab,
          'gasto_jan_gab': gasto_jan_gab,
          'gasto_fev_gab': gasto_fev_gab,
          'gasto_mar_gab': gasto_mar_gab,
          'gasto_abr_gab': gasto_abr_gab,
          'gasto_maio_gab': gasto_maio_gab,
          'gasto_junho_gab' : gasto_junho_gab,
          'gasto_jul_gab' : gasto_jul_gab, 
          'gasto_agosto_gab' : gasto_agosto_gab,
          'gasto_set_gab' : gasto_set_gab,
          'gasto_out_gab' : gasto_out_gab,
          'quant_viagem' : quant_viagem

 
       }


    
        return lista_deputadas
        # O csv de deputadas foi gerado com o comanado scrapy crawl deputadas -o deputadas.csv

