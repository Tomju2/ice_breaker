from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = '''
David Robert Jones (Londres, 8 de enero de 1947-Nueva York, 10 de enero de 2016), más conocido por su nombre artístico David Bowie, fue un cantautor, actor, multiinstrumentista y diseñador británico. Figura importante de la música popular durante casi cinco décadas, Bowie es considerado un innovador, en particular por sus trabajos de la década de 1970 y por su peculiar voz, además de la profundidad intelectual de su obra

Nacido en Brixton, en el sur de Londres, Bowie mostró gran interés por la música en su niñez, estudiando arte, música y diseño antes de embarcarse en su carrera profesional como músico en 1963. A pesar de haber lanzado un álbum (David Bowie) y varios sencillos, Bowie consiguió notoriedad en julio de 1969, cuando su sencillo «Space Oddity» llegó al top 5 de la lista británica de sencillos. Después de tres años con una etapa de experimentación, resurgió en 1972, en plena era del glam rock, con su extravagante y andrógino alter ego Ziggy Stardust, gracias a su exitoso sencillo «Starman» y el disco The Rise and Fall of Ziggy Stardust and the Spiders from Mars. David Buckley, su biógrafo, describe el impacto de Bowie de esa época diciendo que «retó al núcleo de la música rock de la época» y «creó, posiblemente, el personaje más importante de la cultura popular».11​ La corta vida de Ziggy probó ser solo una faceta de una carrera marcada por continuas reinvenciones, innovaciones musicales y presentaciones visuales de todo tipo.

Bowie consiguió, en 1975, su primer éxito número uno en los Estados Unidos, gracias a su exitoso sencillo «Fame», coescrito con John Lennon y a su disco Young Americans, del cual dijo él mismo que era el disco definitivo del plastic soul (término acuñado por un músico de raza negra para describir a un artista blanco interpretando música soul). El sonido significó un cambio radical del estilo que le había hecho famoso en el Reino Unido, aun así el álbum Young Americans llegó al número 1 en las listas de Melody Maker y ese año consiguió otro número 1 con el relanzamiento de Space Oddity, llegó a la posición más alta en las tres listas principales del Reino Unido, su segundo sencillo fue número 1 en Melody Maker y NME, tras The Jean Genie, y ese año logró su segundo sencillo número 1 en Nueva Zelanda con "Young Americans", tras el rotundo éxito de "Sorrow". Después de esto, confundió tanto a su discográfica como a sus seguidores estadounidenses con el disco minimalista Low (1977), la primera de tres colaboraciones con Brian Eno. Todos estos álbumes, conocidos como la «Trilogía de Berlín», entraron en el top 5 británico, además de recibir elogios de la crítica.

Después de dispares éxitos comerciales a finales de la década de 1970, consiguió números uno en el Reino Unido con el sencillo «Ashes to Ashes» y su correspondiente álbum, Scary Monsters (and Super Creeps). Colaboró con Queen en el número uno de las listas de venta «Under Pressure» para, poco después, volver a conseguir un éxito comercial con su disco de 1983 Let's Dance, del que se extrajeron los exitosos sencillos «Let's Dance», «China Girl» y «Modern Love». A lo largo de las décadas de 1990 y 2000, Bowie siguió experimentando con distintos estilos musicales, incluyendo blue-eyed soul, industrial, adult contemporary, jungle y R&B. No salió de gira desde su gira musical entre 2003 y 2004 A Reality Tour y no se presentó en vivo desde 2006. Su más reciente disco Blackstar salió al mercado el 8 de enero de 2016, dos días antes de fallecer.

Buckley dice de Bowie: «Su influencia fue única en la cultura popular, ha permeado y cambiado más vidas que ninguna otra figura pública» En la encuesta de 2002 de la cadena televisiva BBC de los 100 británicos más importantes, se colocó en el puesto número 29. Ha vendido cerca de 136 millones de discos. Ha recibido nueve discos de platino, once de oro y ocho de plata en el Reino Unido y cinco de platino y siete de oro en los Estados Unidos. En 2004, la revista Rolling Stone le posicionó en el puesto 39 entre los cien artistas más importantes de todos los tiempos, y en 23 de los mejores cantantes
'''

if __name__ == "__main__":
    print("holaaaaaaa")

    summary_template = """
    given the information {information} about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables = 'information', template = summary_template)

    llm = ChatOpenAI(temperature=0, model_name = 'gpt-3.5-turbo')

    chain = summary_prompt_template | llm

    response = chain.invoke(input = {'information':information})

    print(response)