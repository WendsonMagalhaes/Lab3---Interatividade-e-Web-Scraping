from wsgiref import headers
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
import scrapy
import pandas as pd



class DeputadosSpider(scrapy.Spider):
    name = "deputados"

    def start_requests(self):
        urls = ['https://www.camara.leg.br/deputados/204554',
                'https://www.camara.leg.br/deputados/204521',
                'https://www.camara.leg.br/deputados/204379',
                'https://www.camara.leg.br/deputados/204560',
                'https://www.camara.leg.br/deputados/121948',
                'https://www.camara.leg.br/deputados/74646',
                'https://www.camara.leg.br/deputados/141372',
                'https://www.camara.leg.br/deputados/160508',
                'https://www.camara.leg.br/deputados/136811',
                'https://www.camara.leg.br/deputados/178835',
                'https://www.camara.leg.br/deputados/160527',
                'https://www.camara.leg.br/deputados/204495',
                'https://www.camara.leg.br/deputados/204549',
                'https://www.camara.leg.br/deputados/178836',
                'https://www.camara.leg.br/deputados/160559',
                'https://www.camara.leg.br/deputados/204413',
                'https://www.camara.leg.br/deputados/204501',
                'https://www.camara.leg.br/deputados/160511',
                'https://www.camara.leg.br/deputados/178972',
                'https://www.camara.leg.br/deputados/204571',
                'https://www.camara.leg.br/deputados/105534',
                'https://www.camara.leg.br/deputados/204544',
                'https://www.camara.leg.br/deputados/160545',
                'https://www.camara.leg.br/deputados/204503',
                'https://www.camara.leg.br/deputados/178833',
                'https://www.camara.leg.br/deputados/198783',
                'https://www.camara.leg.br/deputados/161550',
                'https://www.camara.leg.br/deputados/207309',
                'https://www.camara.leg.br/deputados/132504',
                'https://www.camara.leg.br/deputados/204537',
                'https://www.camara.leg.br/deputados/160640',
                'https://www.camara.leg.br/deputados/204482',
                'https://www.camara.leg.br/deputados/178871',
                'https://www.camara.leg.br/deputados/178930',
                'https://www.camara.leg.br/deputados/178953',
                'https://www.camara.leg.br/deputados/211866',
                'https://www.camara.leg.br/deputados/141428',
                'https://www.camara.leg.br/deputados/68720',
                'https://www.camara.leg.br/deputados/178969',
                'https://www.camara.leg.br/deputados/141427',
                'https://www.camara.leg.br/deputados/171623',
                'https://www.camara.leg.br/deputados/204368',
                'https://www.camara.leg.br/deputados/160587',
                'https://www.camara.leg.br/deputados/66828',
                'https://www.camara.leg.br/deputados/204477',
                'https://www.camara.leg.br/deputados/72442',
                'https://www.camara.leg.br/deputados/204398',
                'https://www.camara.leg.br/deputados/204371',
                'https://www.camara.leg.br/deputados/160666',
                'https://www.camara.leg.br/deputados/212504',
                'https://www.camara.leg.br/deputados/213854',
                'https://www.camara.leg.br/deputados/204518',
                'https://www.camara.leg.br/deputados/212625',
                'https://www.camara.leg.br/deputados/204481',
                'https://www.camara.leg.br/deputados/213679',
                'https://www.camara.leg.br/deputados/204439',
                'https://www.camara.leg.br/deputados/204351',
                'https://www.camara.leg.br/deputados/178830',
                'https://www.camara.leg.br/deputados/204412',
                'https://www.camara.leg.br/deputados/204562',
                'https://www.camara.leg.br/deputados/141417',
                'https://www.camara.leg.br/deputados/134812',
                'https://www.camara.leg.br/deputados/74655',
                'https://www.camara.leg.br/deputados/204541',
                'https://www.camara.leg.br/deputados/92346',
                'https://www.camara.leg.br/deputados/204552',
                'https://www.camara.leg.br/deputados/204500',
                'https://www.camara.leg.br/deputados/178977',
                'https://www.camara.leg.br/deputados/141421',
                'https://www.camara.leg.br/deputados/141422',
                'https://www.camara.leg.br/deputados/154919',
                'https://www.camara.leg.br/deputados/204364',
                'https://www.camara.leg.br/deputados/160532',
                'https://www.camara.leg.br/deputados/204389',
                'https://www.camara.leg.br/deputados/178854',
                'https://www.camara.leg.br/deputados/141431',
                'https://www.camara.leg.br/deputados/92699',
                'https://www.camara.leg.br/deputados/204427',
                'https://www.camara.leg.br/deputados/204411',
                'https://www.camara.leg.br/deputados/141434',
                'https://www.camara.leg.br/deputados/191923',
                'https://www.camara.leg.br/deputados/204392',
                'https://www.camara.leg.br/deputados/204510',
                'https://www.camara.leg.br/deputados/204494',
                'https://www.camara.leg.br/deputados/204393',
                'https://www.camara.leg.br/deputados/74200',
                'https://www.camara.leg.br/deputados/115746',
                'https://www.camara.leg.br/deputados/160669',
                'https://www.camara.leg.br/deputados/204473',
                'https://www.camara.leg.br/deputados/204484',
                'https://www.camara.leg.br/deputados/204527',
                'https://www.camara.leg.br/deputados/74374',
                'https://www.camara.leg.br/deputados/204394',
                'https://www.camara.leg.br/deputados/74383',
                'https://www.camara.leg.br/deputados/204575',
                'https://www.camara.leg.br/deputados/204491',
                'https://www.camara.leg.br/deputados/74270',
                'https://www.camara.leg.br/deputados/204365',
                'https://www.camara.leg.br/deputados/160673',
                'https://www.camara.leg.br/deputados/178996',
                'https://www.camara.leg.br/deputados/204516',
                'https://www.camara.leg.br/deputados/178927',
                'https://www.camara.leg.br/deputados/178937',
                'https://www.camara.leg.br/deputados/178881',
                'https://www.camara.leg.br/deputados/204356',
                'https://www.camara.leg.br/deputados/178831',
                'https://www.camara.leg.br/deputados/74471',
                'https://www.camara.leg.br/deputados/204423',
                'https://www.camara.leg.br/deputados/133439',
                'https://www.camara.leg.br/deputados/178882',
                'https://www.camara.leg.br/deputados/204515',
                'https://www.camara.leg.br/deputados/74212',
                'https://www.camara.leg.br/deputados/160553',
                'https://www.camara.leg.br/deputados/73433',
                'https://www.camara.leg.br/deputados/141391',
                'https://www.camara.leg.br/deputados/204414',
                'https://www.camara.leg.br/deputados/160541',
                'https://www.camara.leg.br/deputados/160600',
                'https://www.camara.leg.br/deputados/159237',
                'https://www.camara.leg.br/deputados/74090',
                'https://www.camara.leg.br/deputados/74459',
                'https://www.camara.leg.br/deputados/160665',
                'https://www.camara.leg.br/deputados/160512',
                'https://www.camara.leg.br/deputados/69871',
                'https://www.camara.leg.br/deputados/178975',
                'https://www.camara.leg.br/deputados/204426',
                'https://www.camara.leg.br/deputados/141398',
                'https://www.camara.leg.br/deputados/204499',
                'https://www.camara.leg.br/deputados/204370',
                'https://www.camara.leg.br/deputados/178876',
                'https://www.camara.leg.br/deputados/204488',
                'https://www.camara.leg.br/deputados/141405',
                'https://www.camara.leg.br/deputados/73441',
                'https://www.camara.leg.br/deputados/204496',
                'https://www.camara.leg.br/deputados/204504',
                'https://www.camara.leg.br/deputados/205476',
                'https://www.camara.leg.br/deputados/204490',
                'https://www.camara.leg.br/deputados/141439',
                'https://www.camara.leg.br/deputados/204476',
                'https://www.camara.leg.br/deputados/204440',
                'https://www.camara.leg.br/deputados/74537',
                'https://www.camara.leg.br/deputados/141408',
                'https://www.camara.leg.br/deputados/204376',
                'https://www.camara.leg.br/deputados/204378',
                'https://www.camara.leg.br/deputados/204514',
                'https://www.camara.leg.br/deputados/178963',
                'https://www.camara.leg.br/deputados/135054',
                'https://www.camara.leg.br/deputados/204355',
                'https://www.camara.leg.br/deputados/141411',
                'https://www.camara.leg.br/deputados/74467',
                'https://www.camara.leg.br/deputados/109429',
                'https://www.camara.leg.br/deputados/141335',
                'https://www.camara.leg.br/deputados/204358',
                'https://www.camara.leg.br/deputados/178948',
                'https://www.camara.leg.br/deputados/204388',
                'https://www.camara.leg.br/deputados/141513',
                'https://www.camara.leg.br/deputados/204561',
                'https://www.camara.leg.br/deputados/204397',
                'https://www.camara.leg.br/deputados/160538',
                'https://www.camara.leg.br/deputados/74052',
                'https://www.camara.leg.br/deputados/204551',
                'https://www.camara.leg.br/deputados/204502',
                'https://www.camara.leg.br/deputados/93083',
                'https://www.camara.leg.br/deputados/204352',
                'https://www.camara.leg.br/deputados/204572',
                'https://www.camara.leg.br/deputados/178829',
                'https://www.camara.leg.br/deputados/204531',
                'https://www.camara.leg.br/deputados/178924',
                'https://www.camara.leg.br/deputados/204487',
                'https://www.camara.leg.br/deputados/141401',
                'https://www.camara.leg.br/deputados/204361',
                'https://www.camara.leg.br/deputados/178962',
                'https://www.camara.leg.br/deputados/178993',
                'https://www.camara.leg.br/deputados/204460',
                'https://www.camara.leg.br/deputados/74262',
                'https://www.camara.leg.br/deputados/74060',
                'https://www.camara.leg.br/deputados/178916',
                'https://www.camara.leg.br/deputados/204367',
                'https://www.camara.leg.br/deputados/204454',
                'https://www.camara.leg.br/deputados/204409',
                'https://www.camara.leg.br/deputados/160528',
                'https://www.camara.leg.br/deputados/62881',
                'https://www.camara.leg.br/deputados/160552',
                'https://www.camara.leg.br/deputados/116379',
                'https://www.camara.leg.br/deputados/73891',
                'https://www.camara.leg.br/deputados/205548',
                'https://www.camara.leg.br/deputados/204511',
                'https://www.camara.leg.br/deputados/204451',
                'https://www.camara.leg.br/deputados/178908',
                'https://www.camara.leg.br/deputados/204512',
                'https://www.camara.leg.br/deputados/204569',
                'https://www.camara.leg.br/deputados/164359',
                'https://www.camara.leg.br/deputados/204542',
                'https://www.camara.leg.br/deputados/213856',
                'https://www.camara.leg.br/deputados/160588',
                'https://www.camara.leg.br/deputados/178929',
                'https://www.camara.leg.br/deputados/160599',
                'https://www.camara.leg.br/deputados/143632',
                'https://www.camara.leg.br/deputados/160758',
                'https://www.camara.leg.br/deputados/204450',
                        
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        nome = response.css("ul.informacoes-deputado").getall()
        nome_deputado = Selector(text=nome[0]).xpath('//li/text()').get()

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

         

        lista_deputados ={
          'nome':nome_deputado,
          'genero':"M",
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



        
    
        return lista_deputados
        # O csv de deputados foi gerado com o comanado scrapy crawl deputados -o deputados.csv
