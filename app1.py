import streamlit as st
from styling import apply_portfolio_styles
from PIL import Image
import base64
import requests
from io import BytesIO


st.set_page_config(
    page_title="Aly Guinga - Portfolio", 
    page_icon="👨‍💻", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# https://materializecss.com/
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">', unsafe_allow_html=True)
# https://materializecss.com/icons.html
st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">', unsafe_allow_html=True)
# https://fontawesome.com/start
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)



#@st.cache_resource(allow_output_mutation=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg_for_main(png_file1):
    bin_str = get_base64_of_bin_file(png_file1)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    backgound-position: center;
    }
    </style>'''% bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg_for_main("images/pexels-eberhardgross-1287142.jpg")

# def set_png_as_page_bg_for_sidebar(png_file1):
#     bin_str = get_base64_of_bin_file(png_file1)
#     page_bg_img = '''
#     <style>
#     .stSidebar {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     backgound-position: center;
#     background-repeat: no-repeat;
#     }
#     </style>'''%bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg_for_sidebar("bg2.jpg")


app_style = """
<style>
[data-testid="stHeader"]    {
    background-color: rgba(0, 0, 0, 0);
    background-size: cover;
}
</style>
"""
st.markdown(app_style, unsafe_allow_html=True)


#pdf functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href


st.markdown("""<style>.centered {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown('<h1 class="centered" style = "background-color:whit;">Aly <span class="blue-text text-darken-3">Guinga</span> </h1>', unsafe_allow_html=True)
st.markdown('<h6 class="centered" style = "background-color:whit;">Étudiant en cycle ingénieur <br>spécialisé en science des données, big data et intelligence artificielle</h6>', unsafe_allow_html=True)

image = "C:/Users/aligu/Desktop/else/portfolio/images/image1c.jpg"
text = "Je suis un étudiant en cycle ingénieur à l'<abbr title= 'École Nationale des Sciences Appliquées'>ENSA</abbr> Tétouan, spécialisé en science des données, big data et intelligence artificielle, passionné par les technologies innovantes et les applications de l'IA dans différents domaines de l'industrie. Je cherche un stage PFA pour appliquer mes connaissances et contribuer à des projets ambitieux. Motivé à apprendre de nouveaux concepts et technologies, je souhaite développer mes compétences dans différents domaines de l'IA et du traitement des données. Je suis ouvert sur tous les projets dans le domaine des sciences de données, vision par ordinateur, <abbr title='Large language models'>LLMs</abbr>, <abbr title='Natural Language Processing'>NLP</abbr> et <abbr title = 'Business intelligence' >BI</abbr>  et tous les autres domaines de l'IA. Prêt à relever des défis techniques, je vise à approfondir mon expertise tout en apportant une réelle valeur ajoutée à votre équipe."
linkedin_url = "https://www.linkedin.com/in/ali-guinga-43770820b/?originalSubdomain=ma"
github_url = "https://github.com/Guinga6"
kaggle_url = "https://www.kaggle.com/aliguinga5"
    
def image_to_base64(parth):
        
# Open the image file in binary mode
    with open("images/image1c.jpg", "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')

# Print the Base64 string (use it in HTML)
    return  base64_string
    
imagebase64  = image_to_base64(image)

profileHTML=f"""
<div class="row">
</div>
<div class="row">
    <div class="col s12 m12">
        <div class="card">
            <div class="card-content">
                <div class="row">                    
                    <div class="col s12 m2">
                        <img class="circle responsive-img" src="data:image/jpeg;base64,{imagebase64}" style="width: 300px; height: 200px;">
                    </div>
                        <div class="col s12 m10 ">
                            <span class="card-title">About me</span>
                            <p>{text}</p>
                            <div class="card-action">
                            <a href="{linkedin_url}" class="blue-text text-darken-3"><i class="fa-brands fa-linkedin fa-2xl"></i></i></a>
                            <a href="{github_url}" class="blue-text text-darken-3"><i class="fa-brands fa-github fa-2xl"></i></a>
                            <a href="{github_url}" class="blue-text text-darken-3"><i class="fa-brands fa-kaggle fa-2xl"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
            """
# Mostramos el HTML generado
st.html(profileHTML)
        

TechnicalSkills, Education, Projects, Competitions, Volunteering, Resume, Contact = st.tabs(["Technical Skills", "Education", "Projects", "Competitions", "Volunteering", "Resume", "Contact"])

        #st.write('Je suis passionné par le machine learning, la science des données et l\'analyse prédictive. Mon objectif est de collaborer avec des experts pour créer des solutions innovantes ayant un impact positif sur la société. Je souhaite rejoindre une équipe dynamique pour partager mes idées et apprendre des autres, tout en restant à l\'affût des dernières tendances en IA.')

with Education:
    
    st.write("\n")
    def image_to_base64(path):
        
# Open the image file in binary mode
        with open(path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        return  base64_string
    
    schools = ['<p style="font-size:110%;"><b>Lycée Ibn Al-atir</b></p>', 
               '<p style="font-size:110%;"><b>Ecole Supérieure de Technologie de Salé</b></p> ', 
               '<p style="font-size:110%;"><b>Cycle Préparatoire Ensa Tétouan</b></p>', 
               '<p style="font-size:110%;"><b>Cycle D\'ingénieur Ensa Tétouan</b></p>']
    
    # Use relative paths instead of absolute paths
    images = ["schoolimage/lycee.jpg", "schoolimage/est.jpg", "schoolimage/ensa.jpg", "schoolimage/ensa.jpg"]
    
    text = ['<p style="font-size:110%"><b>Bac Sciences Physiques</b></p>', 
            '<p style="font-size:110%"><b>Génie civil </b></p>', 
            '<p style="font-size:110%"><b>Deux Années Preparatoire</b></p>',
            '<p style="font-size:110%"><b>Sciences des Données, Big Data & Intelligence Artificielle</b></p>']
    
    duration = ["<p><b>2017 - 2020</b></p>", "<p><b>2020 - 2021</b></p>", "<p><b>2021 - 2023</b></p>", "<p><b>2023 - 2026</b></p>"]
    
    school_url = ["",
                 "https://www.est.um5.ac.ma/formation/dut-genie-civil",
                 "https://ensa-tetouan.ac.ma/annees-preparatoires/", 
                 "https://ensa-tetouan.ac.ma/science-des-donnees-big-data-intelligence-artificielle/"]
    
    for i in range(1, len(schools)+1):
        try:
            
            n = len(schools)
            profileHTML=f"""
            <div class="col s12 m4 l8" >
    <div class="card horizontal" style="margin: 20px; max-height: 300px;">
        <div class="card-image">
            <img class="responsive-img" src="data:image/jpeg;base64,{image_to_base64(images[-i])}" style="width: 250px; height: 200px; object-fit: cover;">
        </div>
        <div class="card-stacked">
            <div class="card-content" style="padding: 15px;">
                <span class="card-title" style="font-size: 1.2rem; margin-bottom: 5px;">{schools[-i]}</span>
                <div class="row" style="margin-bottom: 5px;">
                    <div class="col s12 m9">
                        <h6 style="color:gray; font-size: 0.9rem;"><br>Filière : <br>{text[-i]}</h6>
                    </div>
                    <div class="col s12 m3">
                        <h6 style="color:gray; font-size: 0.9rem;"><br>Durée : {duration[-i]}</h6>
                    </div>
                </div>
            </div>
            <div class="card-action" style="padding: 10px;">
                <a href="{school_url[-i]}" class="blue-text text-darken-3"><i class="fas fa-globe fa-2xl"></i></a>
            </div>
        </div>
    </div>
</div>"""
            st.markdown(profileHTML, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error processing item {i}: {str(e)}")

# Custom styles
customStyle = """
    <style type="text/css">
    /*Aumenta el tamaño de las cards*/
    .card.large{
        height:550px!important;
    }
    /*Aumenta el contenido disponible*/
    .card.large .card-content{
        max-height:fit-content!important;
    }
    /* Aumenta la fuente de los tabs de Streamlit*/
    button[data-baseweb="tab"] p{
        font-size:20px!important;
    }
    /* Remueve el espacio en el encabezado por defecto de las apps de Streamlit */
    div[data-testid="stAppViewBlockContainer"]{
        padding-top:0px;
    }
    </style>
    """
st.markdown(customStyle, unsafe_allow_html=True)

with Projects:

    st.write("\n")

    projects=""
    skillsHTML=""
    knowledgeHTML=""
    projectid= [1, 2, 3, 4]
    project=["Chic-illo AI assistant for recycling", "Analyse BI pour l’Aide à la Décision dans le Partage de Vélos", "Olympic Games Paris 2024 App", "Détection d'objets"]       
    projectName = ["Chic-illo AI assistant for recycling", "Analyse BI pour l’Aide à la Décision dans le Partage de Vélos", "Olympic Games Paris 2024 App", "Détection d'objets"]       
    projectDescription = ["Chic-illo is an AI assistant that helps users recycle waste properly. It uses computer vision to identify objects and provide recycling instructions. The goal is to reduce waste contamination and promote sustainable practices.",
                        "This project is designed to bring the excitement, history, and data of the Olympic Games right to your screen. Whether you're a sports enthusiast, a data nerd, or just curious about the 2024 Olympics, this app has something for everyone.",
                        "This project is designed to bring the excitement, history, and data of the Olympic Games right to your screen. Whether you're a sports enthusiast, a data nerd, or just curious about the 2024 Olympics, this app has something for everyone.",
                        "This project is designed to bring the excitement, history, and data of the Olympic Games right to your screen. Whether you're a sports enthusiast, a data nerd, or just curious about the 2024 Olympics, this app has something for everyone."]   
    projectSkils = [["Python", "Machine Learning", "Deep Learning"], ["Deep Learning", "Data Analysis", "Data Visualization", "SQL"], [ "Data Analysis", "Data Visualization", "SQL"], ["Python", "Machine Learning", "Deep Learning", "Data Analysis", "Data Visualization", "SQL"]]
    projectKnowledge = [["Llm", "streamlite", "Fine-tuning"], [ "Data Analysis", "Data Visualization", "SQL"], [ "Deep Learning", "Data Analysis", "Data Visualization", "SQL"], ["Python", "Machine Learning", "Deep Learning", "Data Analysis", "Data Visualization", "SQL"]]
    projectLink = ["https://github.com", "https://github.com", "https://github.com", "https://github.com"]
    projectimageurl  = ["https://raw.githubusercontent.com/Guinga6/Olympic-Games-Paris-2024/refs/heads/main/data/Screenshot%202024-08-26%20045955.png", "", "","https://media.licdn.com/dms/image/v2/D4E2DAQG-uDrV-wH5Cg/profile-treasury-image-shrink_1280_1280/profile-treasury-image-shrink_1280_1280/0/1722818309915?e=1739631600&v=beta&t=x7A3ZyzulM6kxnpPr6ZaJypa2YXsqKsUcoFay3uuSdM"]
    # Hacemos el ciclo creando las plantillas de proyectos
    for i in range(len(projectid)):
        # st.write(skill['fields'])
    # Creamos la lista de Skills y Knowledge
        skillsHTML=[f'<div class="chip blue lighten-4">{p}</div>' for p in projectSkils[i]]
        skillsHTML="".join(skillsHTML)
        knowledgeHTML=[f'<div class="chip blue lighten-4">{p}</div>' for p in projectKnowledge[i]]
        knowledgeHTML="".join(knowledgeHTML)
        
        st.markdown("""
<style>
/* Grid system */
.col.s12 { width: 100%; }
.col.m6 { width: 50%; }

/* Card styles */
.card.large {
    background-color: white;
    border-radius: 2px;
    box-shadow: 0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2);
    margin: 0.5rem 0 1rem 0;
    transition: box-shadow .25s;
}

.card-image {
    position: relative;
    height: 200px;
}

.card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.card-content {
    padding: 24px;
}

.card-title {
    font-size: 24px;
    font-weight: 300;
    margin-bottom: 16px;
    display: block;
}

.card-action {
    padding: 16px 24px;
    border-top: 1px solid rgba(160,160,160,0.2);
    text-align: right;
}

/* Button styles */
.btn-large {
    text-decoration: none;
    color: white;
    background-color: #1565C0;
    text-align: center;
    letter-spacing: .5px;
    padding: 0 28px;
    height: 54px;
    line-height: 54px;
    border-radius: 2px;
    display: inline-block;
}

.waves-effect {
    position: relative;
    cursor: pointer;
    overflow: hidden;
    user-select: none;
    z-index: 1;
}

/* Hide on small only */
@media only screen and (max-width: 600px) {
    .hide-on-small-only {
        display: none !important;
    }
}

/* Row and column layout */
.row {
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 20px;
}

.row:after {
    content: "";
    display: table;
    clear: both;
}

.col {
    float: left;
    padding: 0 0.75rem;
    min-height: 1px;
}
</style>
""", unsafe_allow_html=True)
        
        # Plantilla de proyectos
        projectHTML = f"""<div class="col s12 m6">
            <div class="card large z-depth-1 hover-card">                    
                <div class="card-image" style="height:200px">
                    <a href="{projectLink[i]}"><img src="{projectimageurl[i]}"></a>
                </div>                        
                <div class="card-content"> 
                <span class="card-title" >{projectName[i]}</span>                                               
                    <p>{projectDescription[i]}</p>
                       <h6>Skills:</h6><hr>
                            {skillsHTML}
                </div>  
                <div class="card-action right-align">
                    <a href="{projectLink[i]}" class="waves-effect waves-light btn-large white-text blue darken-3">
                        <i class="material-icons left">open_in_new</i>View
                    </a>                        
                </div>                                               
            </div>
        </div>"""
        projects=projects+projectHTML
    projectsHTML=f"""
            <div class="row">            
                {projects}       
            </div>       
        """     
    # Mostramos los proyectos
    st.html(projectsHTML) 
    


with Competitions:
    st.write("\n")
    
    st.subheader("Hackathon Eau, l’Environnement et la Sécurité Alimentaire",divider=True)
    st.write("\n")

    with st.container():

        c1, c2 = st.columns((2,3))
        with c1:
            st.image("images/hackathontange.jpg") #, width=300)

        with c2:
            st.markdown('<h5>About the competition</h5>', unsafe_allow_html=True)
            st.write("Le Hackathon Eau, Environnement et Sécurité Alimentaire a été organisé par l'ENSA de Tanger, la Région Tanger-Tétouan-Al Hoceima et le WEF Nexus Forum Tangier 2024. Cet événement s'est tenu les 6 et 7 décembre 2024 à l'ENSA de Tanger, en marge de la deuxième édition du Forum Nexus Eau-Énergie-Alimentation. Il avait pour objectif d'encourager les étudiants à développer des solutions innovantes face aux défis liés à l'eau, à l'environnement et à la sécurité alimentaire.")
            col1, col2 = st.columns((1,1))
            with col1:
                st.markdown('<h5>Les Prixs</h5>', unsafe_allow_html=True)
                st.write("🥇 1er Prix: *40 000* MAD")
                st.write("🥈 2ème Prix: *30 000* MAD")
                st.write("🥉 3ème Prix: *20 000* MAD")
            with col2:
                st.markdown('<h5>Notre Progres</h5>', unsafe_allow_html=True)
                st.write("On a presenté le projet *Chic-illo* dans le cadre de ce hackathon (Voire Les Projet). dans les deux phases de la compétition, nous avons été sélectionnés parmi les 10 meilleurs porjets pour la Semi-finale.")

                #st.write("On a presenté un projet qui a pour but de réduire la consommation d'eau dans les foyers marocains. Notre solution est basée sur l'analyse des données de consommation d'eau et la prédiction des fuites d'eau.")
    st.write("###")

    st.subheader("Competition 2: Kaggle Titanic: Machine Learning from Disaster", divider=True)
    


with Resume: 

    st.write("\n")
      
    resume_url = "https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing"
  
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("attributiondesexposés-filliereBD&AI.pdf")
    with open("attributiondesexposés-filliereBD&AI.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (1 page)",
            data=file,
            file_name="attributiondesexposés-filliereBD&AI.pdf",
            mime="application/pdf"
        )

with TechnicalSkills:
    
    st.write("###")
    competences = [
    "Python", "Langage R", "Java", "SQL",
    "Pandas", "NumPy", "Selenium", "PyTorch", "BeautifulSoup",
    "Word", "PowerPoint", "Excel"
]

    descriptions = [
    "On utilise Python comme langage principal dans le processus de manipulation de données, dans lequel on effectue le traitement de données et la création de modèles de machine learning avec des bibliothèques Python spécifiques.",
    
    "R est particulièrement puissant pour l'analyse statistique et la visualisation de données. Il offre un environnement spécialisé pour l'analyse statistique avec des packages comme ggplot2 pour la création de graphiques sophistiqués et dplyr pour la manipulation de données.",
    
    "Java est un langage de programmation orienté objet robuste utilisé pour développer des applications d'entreprise scalables. Sa portabilité 'Write Once, Run Anywhere' et sa forte typologie en font un choix excellent pour les applications distribuées.",
    
    "Le langage SQL est fondamental pour la gestion et l'interrogation des bases de données relationnelles. Il permet d'effectuer des requêtes complexes, de manipuler les données et de gérer les structures de bases de données.",
    
    "Cette bibliothèque Python est essentielle pour la manipulation et l'analyse de données structurées. Elle offre des structures de données puissantes comme les DataFrames et les Series, permettant une manipulation efficace des données tabulaires.",
    
    "NumPy constitue la base du calcul scientifique en Python. Elle fournit des outils pour manipuler des tableaux multidimensionnels et effectuer des opérations mathématiques complexes de manière efficace.",
    
    "Cet outil d'automatisation permet le test et le scraping de sites web. Il permet d'interagir programmatiquement avec des pages web, d'automatiser des tests d'interface utilisateur et de collecter des données à partir de sources web dynamiques.",
    
    "Ce framework de deep learning offre une approche dynamique pour la construction et l'entraînement de réseaux de neurones. Il est particulièrement apprécié pour sa flexibilité dans la recherche en apprentissage profond.",
    
    "Cette bibliothèque Python est spécialisée dans le parsing de documents HTML et XML. Elle simplifie grandement l'extraction de données à partir de pages web, permettant une analyse efficace du contenu web structuré.",
    
    "Microsoft Word est un logiciel de traitement de texte complet permettant la création et l'édition de documents professionnels. Il offre des fonctionnalités avancées de mise en page et de révision.",
    
    "Cet outil de présentation permet de créer des supports visuels impactants pour la communication professionnelle. Il combine des fonctionnalités de design, d'animation et de présentation.",
    
    "Microsoft Excel est un outil puissant pour l'analyse de données et la création de tableaux de bord. Il permet la manipulation de données, l'analyse statistique et la création de graphiques."
]

    niveaux = [
    "★★★☆☆", "★★☆☆☆", "★☆☆☆☆", "★★★☆☆",
    "★★★☆☆", "★★★☆☆", "★★★☆☆", "★★☆v☆", "★★☆☆☆",
    "★★☆☆☆", "★★★☆☆", "★★★☆☆"
]

    depuis = [
    "2021 - 3 ans", "2020 - 4 ans", "2019 - 5 ans", "2020 - 4 ans",
    "2021 - 3 ans", "2021 - 3 ans", "2022 - 2 ans", "2022 - 2 ans", "2022 - 2 ans",
    "2018 - 6 ans", "2018 - 6 ans", "2018 - 6 ans"
]
    
    icon_map = {
    "Python": "fab fa-python",
    "Langage R": "fas fa-calculator",
    "Java": "fab fa-java",
    "SQL": "fas fa-database",
    "Pandas": "fas fa-table",
    "NumPy": "fas fa-superscript",
    "Selenium": "fas fa-robot",
    "PyTorch": "fas fa-brain",
    "BeautifulSoup": "fas fa-code",
    "Word": "fas fa-file-word",
    "PowerPoint": "fas fa-file-powerpoint",
    "Excel": "fas fa-file-excel"
}

    def html(i):
        
        skillHTML = f"""<div class="col s12 m4">
                <div class="card small">
                    <!-- Add the card-image div here -->
                    <div class="card-content">
                        <span class="card-title"> {competences[i]} 
                        <i class="{icon_map[competences[i]]} right "></i>
                        </span>
                        <p>{descriptions[i]}</p>
                    </div>                      
                    <div class="card-action">
                        <div class="col s12 m6">
                            <p>Level:<br/> {niveaux[i]}</p>
                        </div>
                        <div class="col s12 m6">
                            <p fon>Since:<br/> {depuis[i]} years</p>
                        </div>
                    </div>
                </div>
            </div>"""
        
        return skillHTML
    
    skill1, skill2,skill3,skill4  = "", "", "", ""
    for i in range(len(depuis)):
        #image = base64.b64encode(open(icons[i], "rb").read()).decode()
        if i<3:
            skillHTML1 = html(i)
            skill1=skill1 +skillHTML1
            
        elif i == 3:
            skillHTML2 = html(i)
            skill2=skill2 +skillHTML2
            
        elif i>3 and i<9:
            skillHTML3 = html(i)
            skill3=skill3 +skillHTML3
        else:
            skillHTML4 = html(i)
            skill4=skill4 +skillHTML4

    htmls = [skill1, skill2, skill3, skill4]
    type = ["Language de Programation",  "Language de Base de donnees", "Biblio", "Microsoft Office"]
    st.html('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">')
    for i in range(4):
        st.subheader(type[i], divider=True)
        skillsHTML=f"""
                    <div class="row">            
                        {htmls[i]}       
                    </div>       
                """     
            # Mostramos los skills
        st.html(skillsHTML)
         
