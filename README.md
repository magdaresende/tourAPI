# tourAPI

* Requisitos:

	* Python 3.6
	* flask
	* jsonify

		pip install -r requirements.txt  (instala as depedências necessárias (flask e jsonify))


* Ficheiros:
	
	**tour_api.py:** API que recebe a origem e o destino de uma viagem e devolve os pontos de interesse. Ou recebe duas coordenadas (latitude e longitude) e devolve o ponto de interesse mais próximo.
	
	**table-schemes.txt:** Estrutura da base de dados
	
	**tour.db:** base de dados sqlite

* Correr a aplicação:
	
		python tour_api.py

* Utilização: (assumindo http://127.0.0.1:5000 como o endereço onde corre a aplicação)
	
	Para obter os pontos de interesse de uma viagem:

		http://127.0.0.1:5000/trip/<origem>/<destino>
		
		exemplos: http://127.0.0.1:5000/trip/Lisboa/Algarve
					http://127.0.0.1:5000/trip/Sintra/Lisboa

	Para obter ponto de interesse mais próximo:

		http://127.0.0.1:5000/highlight/<latitude>/<longitude>
		
		exemplos: http://127.0.0.1:5000/highlight/10.3/5
					http://127.0.0.1:5000/highlight/20/5
