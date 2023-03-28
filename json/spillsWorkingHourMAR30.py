import csv 
import json
import os, math
import numpy as np

idNumber=["QAI_DK1001",
"QAI_DK1003",
"QAI_DK1004",
"QAI_DK1005",
"QAI_DK1009",
"QAI_DK1010",
"QAI_DK1011",
"QAI_DK1014",
"QAI_DK1018",
"QAI_DK1019",
"QAI_DK1020",
"QAI_DK1021",
"QAI_DK1022",
"QAI_DK1023",
"QAI_DK1024",
"QAI_DK1025",
"QAI_DK1038",
"QAI_DK1039",
"QAI_DK1040",
"QAI_DK1041",
"QAI_DK1042",
"QAI_DK1043",
"QAI_DK1044",
"QAI_DK1045",
"QAI_DK1046",
"QAI_DK1047",
"QAI_DK1048",
"QAI_DK1049",
"QAI_DK1050",
"QAI_DK1051",
"QAI_DK1052",
"QAI_DK1053",
"QAI_DK1054",
"QAI_DK1055",
"QAI_DK1056",
"QAI_DK1057",
"QAI_DK1058",
"QAI_DK1059",
"QAI_DK1060",
"QAI_DK1061",
"QAI_DK1062",
"QAI_DK1063",
"QAI_DK1064",
"QAI_DK1065",
"QAI_DK1066",
"QAI_DK1067",
"QAI_DK1068",
"QAI_DK1069",
"QAI_DK1070",
"QAI_DK1071",
"QAI_DK1072",
"QAI_DK1073",
"QAI_DK1074",
"QAI_DK1075",
"QAI_DK1076",
"QAI_DK1077",
"QAI_DK1078",
"QAI_DK1079",
"QAI_DK1080",
"QAI_DK1081",
"QAI_DK1082",
"QAI_DK1083",
"QAI_DK1084",
"QAI_DK1085",
"QAI_DK1086",
"QAI_DK1087",
"QAI_DK1088",
"QAI_DK1089",
"QAI_DK1090",
"QAI_DK1091",
"QAI_DK1092",
"QAI_DK1093",
"QAI_DK1094",
"QAI_DK1095",
"QAI_DK1096",
"QAI_DK1097",
"QAI_DK1098",
"QAI_DK1099",
"QAI_DK1100",
"QAI_DK1037",
"QAI_DK1036",
"QAI_DK1035",
"QAI_DK1034",
"QAI_CD1001",
"QAI_CD1002",
"QAI_CD1003",
"QAI_CD1004",
"QAI_CD1005",
"QAI_CD1006",
"QAI_CD1007",
"QAI_CD1008",
"QAI_CD1009",
"QAI_CD1010",
"QAI_CD1011",
"QAI_CD1012",
"QAI_CD1013",
"QAI_CD1014",
"QAI_CD1015",
"QAI_CD1016",
"QAI_CD1017",
"QAI_CD1018",
"QAI_CD1019",
"QAI_CD1020",
"QAI_CD1021",
"QAI_CD1022",
"QAI_CD1023",
"QAI_CD1024",
"QAI_CD1025",
"QAI_CD1026",
"QAI_CD1027",
"QAI_CD1028",
"QAI_CD1029",
"QAI_CD1030",
"QAI_CD1031",
"QAI_CD1032",
"QAI_CD1033",
"QAI_CD1034",
"QAI_CD1035",
"QAI_CD1036",
"QAI_CD1037",
"QAI_CD1038",
"QAI_CD1039",
"QAI_CD1040",
"QAI_CD1041",
"QAI_CD1042",
"QAI_CD1043",
"QAI_CD1044",
"QAI_CD1045",
"QAI_CD1046",
"QAI_CD1047",
"QAI_CD1048",
"QAI_CD1049",
"QAI_CD1050",
"QAI_CD1051",
"QAI_CD1052",
"QAI_CD1053",
"QAI_CD1054",
"QAI_CD1055",
"QAI_CD1056",
"QAI_CD1057",
"QAI_CD1058",
"QAI_CD1059",
"QAI_CD1060",
"QAI_CD1061",
"QAI_CD1062",
"QAI_CD1063",
"QAI_CD1064",
"QAI_CD1065",
"QAI_CD1066",
"QAI_CD1067",
"QAI_CD1068",
"QAI_CD1069",
"QAI_CD1070",
"QAI_CD1071",
"QAI_CD1072",
"QAI_CD1073",
"QAI_CD1074",
"QAI_CD1075",
"QAI_CD1076",
"QAI_CD1077",
"QAI_CD1078",
"QAI_CD1079",
"QAI_MS1001",
"QAI_MS1002",
"QAI_MS1003",
"QAI_MS1004",
"QAI_MS1005",
"QAI_MS1006",
"QAI_MS1007",
"QAI_MS1008",
"QAI_MS1009",
"QAI_MS1010",
"QAI_MS1011",
"QAI_MS1012",
"QAI_MS1013",
"QAI_MS1014",
"QAI_MS1015",
"QAI_MS1016",
"QAI_MS1017",
"QAI_MS1018",
"QAI_MS1019",
"QAI_MS1020",
"QAI_MS1021",
"QAI_MS1022",
"QAI_MS1023",
"QAI_MS1024",
"QAI_MS1025",
"QAI_MS1026",
"QAI_MS1027",
"QAI_MS1028",
"QAI_MS1029",
"QAI_MS1030",
"QAI_MS1031",
"QAI_MS1032",
"QAI_MS1033",
"QAI_MS1034",
"QAI_MS1035",
"QAI_MS1036",
"QAI_MS1037",
"QAI_MS1038",
"QAI_SG1001",
"QAI_SG1002",
"QAI_SG1003",
"QAI_SG1004",
"QAI_SG1005",
"QAI_SG1006",
"QAI_SG1007",
"QAI_SG1008",
"QAI_SG1009",
"QAI_SG1010",
"QAI_SG1012",
"QAI_SG1013",
"QAI_SG1014",
"QAI_SG1015",
"QAI_SG1016",
"QAI_SG1018",
"QAI_SG1017"
]

resName=["Alvee Musharrat Hridita",
"M Yousup Razu",
"Anwarul Azim Shishir",
"Md.Tousif Rob Chowdhury",
"Tanzina Hassan",
"Md. Towfique Hossain Russell",
"Fouzia	Binte Haque",
"Md. Muyeed Shahriar",
"Asad Uz Zaman",
"Mahedi Hasan Tanvir",
"Toki Tahmid Alve",
"Md. Sorowar Hossen",
"Ashraf Uddin",
"Noushin Sadaf",
"Syed Shahi Imran",
"MdMamunHawladar",
"Shahriar Iqbal ",
"showkeya shaharin shetu",
"Tabassum Kabir",
"Akram Hossain",
"Israt Ahmed Sumaya",
"Saide imran nu",
"tamim",
"Afsara Tasnim",
"Mohammad Samiul Talukder",
"arif khan",
"Md Ashrafur Rahman",
"Sabrina Hossin Raka",
"Jeba Anika Chowdhury ",
"Md. Soikat Ali",
"Rifat hossain",
"Fatema Tuj Johora",
"Al-Amin",
"Md Mehedi hasan",
"Milee Farhana Naz ",
"Md Hasan",
"Jaber Hossain",
"Ahmed Najm Anis",
"Rumel",
"SHANEYAZUL HAQUE",
"Shaikh Md.Mustakim",
"Sheikh Mash-ud Abir",
"Anika Rahman",
"Shide afride shampad",
"Md.Rabiul Awal Shakil",
"Safi Ud Dowla",
"Md. Imran Hossain",
"Md.Mostafizur Rahman",
"Raihan Hossain Hriday ",
"SANJOY CHANDRA BARMAN",
"Ekramul Hasan Sazid",
"Fahmida kabir",
"Md.Mominul Islam",
"Ismail Hossain Shuvo ",
"Sumyia Shikder Safa",
"Md. Naim Ahmed",
"MD. Tanvir Zahid ",
"M Rakibul Islam",
"Salma Hani Nova",
"Abdullah Al Farabe",
"Ahmed Nayeem Uddin",
"Md. Mahfuj Hasan Shohug",
"Ruzmee Amana",
"Riad mhamud",
"Ahamed Shakir",
"Amit Chowdhury",
"Siful Islam",
"Lamia Akter",
"Azim Hossain",
"Md.Sirajul Islam Sojol",
"Umme Jannatul Salma",
"Tazul Islam suzon",
"Anaiya Ahmed Ananna",
"Kamrul hasan",
"Mohammad Abdulla Al Amin",
"Intesar Zaman",
"Zakia Sultana",
"Mohammad Sadman Tahsin ",
"Mohammad Samiul Alam",
"Md.Mostafizur Rahman",
"Sifat Khan",
"Niloy khan",
"Imran Bin Imam",
"Md. Antor Ali",
"Asif Iqbal",
"MD EMON AHMED",
"kibria joarder ",
"Arzu Sultana",
"Suraiya parvin",
"Hamim Hasan",
"Md. Alimul Jony",
"Fattain Naime",
"Ashim Mazumder Santo ",
"Fatema Tuj Johora",
"Kamruzzaman  lizon",
"Nazmus Sakib Rabby",
"Imdadul Hoque Rabbi",
"Afrina tabassum ",
" Shaikh Md.Mustakim",
"Karnophully Mim",
"md shohag gazi ",
"Sabbir Hossain",
"Anika Tasnim",
"Umme Mariam",
"Ronok Khan",
"Salman Abir",
"Mahin Bhuiyan",
"Robiul Islam",
"Rumel",
"Md Nirjon Ahamed Shohan",
"Tanzila Ishran",
"Arif khan",
"B.M. Ashif Shariar (shuvo)",
"md. mahadi hasan palash",
"tamim",
"rojoni islam",
"Bipasha Ahmed",
"Muqaddas Malik",
"Afia Wasima ",
"solayman sweet",
"Tonmoy ahamed",
"Rizwan Ahmed",
"S M Arafath Joy",
"Emran",
"Arup Ratan Sen",
"Rana Malik",
"Shaheb ali",
"Israt Ahmed Sumaya",
"Khalid Imtiaz",
"Md Arafat Hossen ",
"Taslima Tasme",
"Shahriyar pranto",
"Robin",
"enamul",
"Sadik Islam",
"Shetu ahmed",
"Iqbal Hossain",
"Bobita Khatun",
"",
"Ayesha akther",
"Shapon ali",
"Shishir Ahmmed",
"bojlur rahman",
"Ali Adom",
"Farhan Labib",
"Jeba Hoque",
"Md. Meshkatul Haque",
"Israt Jahan",
"MD. Emdadul haque",
"Tanvir Jubair",
"Abu Talha",
"md. Hasibul (Hasib)",
"Rohid Rahman",
"Syed Shanto",
"sumaiya jahan eva",
"Md kazol hossain",
"Nahad RAhman",
"MD. Shihab Hossain Joardar Munim",
"Rupok ahmed",
"Lamia Ferdosh",
"MD Habibur Rahman",
"Sadiqur Ashfaq",
"Md Ebrahim Khalilullah",
"Arman Sarker Nayem",
"Muhammad Mamun Mia",
"Md Soton mia",
"Md rakibul hasan (Dipu)",
"Md. Shahidul Islam Sabbir ",
"Arifujjaman Arif",
"sharful amin masum",
"Sumaya Akter Moury",
"Abdullah Al Ahad",
"Md Shahin Alam",
"Iqbal Hossen Rakib",
"Nasir Uddin ",
"MD Rasel Shekh",
"Amit Chowdhury",
"Toky Tahmid Radit",
"Md Jonayed Hossain",
"Kamrul Hasan",
"Md Sadikur Rahman",
"Mahfuzul haque khan",
"Ishraq Ahmed",
"Md Shohag Ahmed Bulbul",
"Mahjabin Mili",
"Voktibikash Ray",
"Muhammad Mahfuz Alam ",
"Mohidul islam",
"Md. Mahfuj Hasan Shohug",
"Ruzmee Amana",
"Riad mhamud",
"Siful Islam",
"Azim Hossain ",
"Robiul Awal",
"Hasnur Jahan",
"Md Asif Khan",
"Foisal Ahmmed",
"Popy",
"Adon",
"Sumon sarker",
"Atik Hasan",
"Abdullah Yusuf zahid",
"Mamunur Rashid ",
"Imtiaz Ahmed",
"Sabbir Talukder",
"Md. sabuj hossen sorker",
"Md.Nahid Hasan",
"Md.Rifat Hsan ",
"Jaidur Rahman soton",
"Sanjida Hasan Maria",
"Md Arif",
"Md. Erfath Rahman",
"Eity Khatun",
"Mehedi Hasan Shanto",
"Habib ullah ",
"Sajib islam",
"suchi islam"
]


def csv_to_json(csvFilePath, jsonFilePath):
	jsonArray = []
	  
	#read csv file
	with open(csvFilePath, encoding='utf-8') as csvf: 
		#load csv file data using csv library's dictionary reader
		csvReader = csv.DictReader(csvf) 

		#convert each csv row into python dict
		for row in csvReader: 
			#add this python dict to json array
			jsonArray.append(row)
  
	#convert python jsonArray to JSON String and write to file
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
		jsonString = json.dumps(jsonArray, indent=4)
		jsonf.write(jsonString)
		  
csvFilePath = r'csv.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)

path_to_json="ann/"




with open("data.json") as json_file:
	data = json.load(json_file)
	#print(data)
	
	
	dlt=[]
	update=[]
	create=[]
	createTrack=[]
	dltC=0
	updateC=0
	createC=0
	createTrackC=0
	
	n=0
	
	for i in data:
		
		
		if(data[n]["action"]=="disable_figure"):
			dlt.append(data[n]["figureId"])
		if(data[n]["action"]=="create_figure"):
			if(data[n]["meta"]=="{'source': 'tracking'}"):
				createTrack.append(data[n]["figureId"])

			elif(len(data[n]["meta"])>22):
				
				if(data[n]["meta"].split(",")[1]==" 'source': 'tracking'}"):
					#print(data[n]["meta"].split(",")[1])
					createTrack.append(data[n]["figureId"])
				elif(data[n]["meta"].split(",")[1]==" 'source': 'clone_on_next'}"):
					create.append(data[n]["figureId"])
				elif(data[n]["meta"].split(",")[1]==" 'source': 'clone_copy'}"):
					createTrack.append(data[n]["figureId"])

				
				
			else:
				create.append(data[n]["figureId"])

			
		if(data[n]["action"]=="update_figure"):
			update.append(data[n]["figureId"])
		
		n+=1
	
	npDlt=np.array(dlt)
	npCreate=np.array(create)
	npCreateTrack=np.array(createTrack)
	npUpdate=np.array(update)

	#print("totalDltNotUnique:"+str(len(npDlt)))

	npUniquDlt=np.unique(npDlt)
	npUniqueCreate=np.unique(npCreate)
	npUniqueCreateTrack=np.unique(npCreateTrack)
	npUniqueUpdate=np.unique(npUpdate)

	
	#print(len(npUpdate))
	#print(len(npUniqueUpdate))

	npUniquDltInt=[]
	for i in npUniquDlt:
		npUniquDltInt.append(int(float(i)))


	npUniqueCreateInt=[]
	for i in npUniqueCreate:
		npUniqueCreateInt.append(int(float(i)))

	npUniqueCreateTrackInt=[]
	for i in npUniqueCreateTrack:
		npUniqueCreateTrackInt.append(int(float(i)))

	npUniqueUpdateInt=[]
	for i in npUniqueUpdate:
		npUniqueUpdateInt.append(int(float(i)))
	# print("normal Create: "+str(len(npUniqueCreateInt)))
	# print("Track Create: "+str(len(npUniqueCreateTrackInt)))
	totalCreateQA=np.concatenate((npUniqueCreateInt, npUniqueCreateTrackInt))
	

	# print("total create:"+str(len(totalCreateQA)))
	# print("total Dlt Unique: "+str(len(npUniquDltInt)))


	keyIDMap=open('key_id_map.json')
	keys=json.load(keyIDMap)

	fig=[]
	for k in keys["figures"].keys():
		fig.append(keys["figures"][k])
	
	figures=np.array(fig)


	print("current Figure on data: "+str(len(figures)))
	print("initial figure left:"+str(len(np.setdiff1d(figures, totalCreateQA))))



	clientFigure=np.setdiff1d(figures,totalCreateQA)
	acceptedFigure=np.setdiff1d(clientFigure,npUniquDltInt)



	newCreate=np.setdiff1d(totalCreateQA,npUniquDltInt)

	#print(len(acceptedFigure))

	#print("original create: "+str(len(newCreate)))

	
	
	normalCreateOndata=np.intersect1d(npUniqueCreateInt,figures)
	print("normal Create on dataset: "+str(len(normalCreateOndata)))

	trackCreateOnData=np.intersect1d(npUniqueCreateTrackInt,figures)
	print("Track Create on dataset: "+str(len(trackCreateOnData)))

	createPresentonData=np.intersect1d(totalCreateQA,figures)
	print("createFigureon dataset: "+str(len(createPresentonData)))
	
	initialFigureLeft=np.setdiff1d(figures, totalCreateQA)
	print(initialFigureLeft)
	print("initial figure left:"+str(len(initialFigureLeft)))

	actualDelete=np.setdiff1d(npUniquDltInt,totalCreateQA)
	print("delete without create: "+str(len(actualDelete)))

	updateAvaiable=np.concatenate((initialFigureLeft,trackCreateOnData))
	actualUpdate=np.intersect1d(npUniqueUpdateInt,updateAvaiable)
	print("updates exist on dataset:"+str(len(actualUpdate)))

	print(len(totalCreateQA))	
		
	#each labelers Count

	
	labelers=[]
	m=0
	for data1 in data:
		labelerName=data[m]["user"]
		if labelerName not in labelers:
			labelers.append(labelerName)
		m+=1
	l=0
	
	for labeler in labelers:
		dlt=[]
		update=[]
		create=[]
		createTrack=[]
		dltC=0
		updateC=0
		createC=0
		createTrackC=0
		
		n=0
		
		for i in data:
			if(data[n]["user"]==labelers[l]):
				if(data[n]["action"]=="disable_figure"):
					dlt.append(data[n]["figureId"])
				if(data[n]["action"]=="create_figure"):
					if(data[n]["meta"]=="{'source': 'tracking'}"):
						createTrack.append(data[n]["figureId"])

					elif(len(data[n]["meta"])>22):
						
						if(data[n]["meta"].split(",")[1]==" 'source': 'tracking'}"):
							#print(data[n]["meta"].split(",")[1])
							createTrack.append(data[n]["figureId"])
						elif(data[n]["meta"].split(",")[1]==" 'source': 'clone_on_next'}"):
							create.append(data[n]["figureId"])
						elif(data[n]["meta"].split(",")[1]==" 'source': 'clone_copy'}"):
							createTrack.append(data[n]["figureId"])

						
						
					else:
						create.append(data[n]["figureId"])

					
				if(data[n]["action"]=="update_figure"):
					update.append(data[n]["figureId"])
			
			n+=1

		labelerNpDlt=np.array(dlt)
		labelerNpCreate=np.array(create)
		labelerNpCreateTrack=np.array(createTrack)
		labelerNpUpdate=np.array(update)

		#print("totalDltNotUnique:"+str(len(npDlt)))

		labelerNpUniquDlt=np.unique(labelerNpDlt)
		labelerNpUniqueCreate=np.unique(labelerNpCreate)
		labelerNpUniqueCreateTrack=np.unique(labelerNpCreateTrack)
		labelerNpUniqueUpdate=np.unique(labelerNpUpdate)

		
		#print(len(npUpdate))
		#print(len(npUniqueUpdate))

		labelerNpUniquDltInt=[]
		for i in labelerNpUniquDlt:
			labelerNpUniquDltInt.append(int(float(i)))


		labelerNpUniqueCreateInt=[]
		for i in labelerNpCreate:
			labelerNpUniqueCreateInt.append(int(float(i)))

		labelerNpUniqueCreateTrackInt=[]
		for i in labelerNpUniqueCreateTrack:
			labelerNpUniqueCreateTrackInt.append(int(float(i)))

		labelerNpUniqueUpdateInt=[]
		for i in labelerNpUniqueUpdate:
			labelerNpUniqueUpdateInt.append(int(float(i)))
		# print("normal Create: "+str(len(npUniqueCreateInt)))
		# print("Track Create: "+str(len(npUniqueCreateTrackInt)))
		
		

		# print("total create:"+str(len(totalCreateQA)))
		# print("total Dlt Unique: "+str(len(npUniquDltInt)))


		keyIDMap=open('key_id_map.json')
		keys=json.load(keyIDMap)

		fig=[]
		for k in keys["figures"].keys():
			fig.append(keys["figures"][k])
		
		figures=np.array(fig)


		

		#print(labelers[l])
		
		labelerNormalCreateOndata=np.intersect1d(labelerNpUniqueCreateInt,figures)
		#print("normal Create on dataset: "+str(len(labelerNormalCreateOndata)))

		labelertrackCreateOnData=np.intersect1d(labelerNpUniqueCreateTrackInt,figures)
		#print("Track Create on dataset: "+str(len(labelertrackCreateOnData)))


		labeleractualDelete=np.setdiff1d(labelerNpUniquDltInt,totalCreateQA)
		#print("delete without create: "+str(len(labeleractualDelete)))
		#print(len(totalCreateQA))

		labelerupdateAvaiable=np.concatenate((labelertrackCreateOnData,initialFigureLeft))
		labeleractualUpdate=np.intersect1d(labelerNpUniqueUpdateInt,labelerupdateAvaiable)
		#print("updates exist on dataset:"+str(len(labeleractualUpdate)))

		tagCount=0
		for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
			with open(path_to_json + file_name) as json_file:
				annData = json.load(json_file)		
				total=0
				
	
				
				i=0
				for y in annData["objects"]:
					tag=0
					for t in annData["objects"][i]["tags"]:
						if annData["objects"][i]["tags"][tag]["labelerLogin"] == labelers[l]:
							tagCount+=1
							
						tag+=1
					i+=1
					


		index=0
		flag=0
		resindex=0
		resNameeFinal=""
		for i in idNumber:
			if idNumber[index]==labelers[l]:
				resindex=index
				
				flag=1
			index+=1
		
		if flag==0:
			resNameeFinal="Unknown"
		else:
			resNameeFinal=resName[resindex]
		if len(labelerNormalCreateOndata)>1000 and len(labelertrackCreateOnData)==100:
			print(str(resNameeFinal)+":"+str(labelers[l])+": :"+str(len(labelerNormalCreateOndata))+":5: :"+str(len(labeleractualUpdate))+":4: :"+str(len(labelertrackCreateOnData))+":120: :"+str(len(labeleractualDelete))+":1:"+str(tagCount)+":20: "+"RED FLAG")
		else:
			print(str(resNameeFinal)+":"+str(labelers[l])+": :"+str(len(labelerNormalCreateOndata))+":5: :"+str(len(labeleractualUpdate))+":4: :"+str(len(labelertrackCreateOnData))+":120: :"+str(len(labeleractualDelete))+":1:"+str(tagCount)+":20:")
		l+=1
	

	
