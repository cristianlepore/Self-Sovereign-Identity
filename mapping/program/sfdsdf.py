@prefix : <http://example.org/ssi#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:SSIPrinciple rdf:type owl:Class ;
    rdfs:label "Self-Sovereign Identity Principle" .

# Principi fondamentali
:Existence rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Existence" .

:Control rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Control" .

:Access rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Access" .

# Principi operativi
:Persistence rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Persistence" .

:Portability rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Portability" .

:Interoperability rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Interoperability" .

# Principi etici e di sicurezza
:Transparency rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Transparency" .

:Consent rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Consent" .

:Minimization rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Minimization" .

:Protection rdf:type owl:Class ;
    rdfs:subClassOf :SSIPrinciple ;
    rdfs:label "Protection" .

# Relazioni tra i principi
:hasPrerequisite rdf:type owl:ObjectProperty ;
    rdfs:domain :SSIPrinciple ;
    rdfs:range :SSIPrinciple ;
    rdfs:label "has prerequisite" .

:facilitates rdf:type owl:ObjectProperty ;
    rdfs:domain :SSIPrinciple ;
    rdfs:range :SSIPrinciple ;
    rdfs:label "facilitates" .

:isHinderedBy rdf:type owl:ObjectProperty ;
    rdfs:domain :SSIPrinciple ;
    rdfs:range :SSIPrinciple ;
    rdfs:label "is hindered by" .

# Esempi di relazioni tra principi
:Control :hasPrerequisite :Existence .
:Consent :facilitates :Minimization .
:Portability :facilitates :Interoperability .
:Transparency :facilitates :Consent .
