<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.tags_registry"></a>Chapter 42. CommonType Layout tag registry</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm483209005344"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.43.1.1"></a>Specification</h4></div></div></div><p>The tag registry defines the CommonType Layout tags that
	  Microsoft supports. CommonType Layout tags are 4-byte
	  character strings that identify the scripts, language
	  systems, features and baselines in a CommonType Layout
	  font. The registry establishes conventions for naming and
	  using these tags. Registered tags have a specific meaning
	  and convey precise information to developers and
	  text-processing clients of CommonType Layout. Microsoft
	  encourages font developers to use registered tags to assure
	  compatibility and ease of use across fonts, applications,
	  and operating systems. Microsoft will supply a list of
	  additional tags upon request.</p><p>The following sections contain sample sets of commonly
	  used tags for scripts, language systems, and
	  baselines. Microsoft will supply a list of additional tags
	  upon request. In addition, the 'Feature tags' section
	  defines all the feature tags Microsoft has developed and
	  registered to date, including descriptions of the functions
	  of each feature.</p><p>Microsoft expects the list of registered tags and
	  features to expand over time. The most recent version of the
	  registry will be available on Microsoft's ftp and World Wide
	  Web sites.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="ttoreg_basetags"></a>Script tags</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.43.2.1"></a>Specification</h4></div></div></div><p>Script tags identify the scripts represented in a
	  CommonType Layout font. Script tags are defined by Microsoft
	  Typography and correspond to the contiguous character code
	  ranges in Unicode.</p><p>All tags are 4-byte character strings composed of a
	  limited set of ASCII characters in the 0x20-0x7E range. A
	  script tag can consist of four or fewer lowercase
	  letters. If a script tag consists less than four lowercase
	  letters, the letters are followed by the requisite number of
	  spaces (0x20), each consisting of a single byte.</p><p>Some of most commonly used script tags are shown
	  below. A full list of script tags is available from
	  Microsoft.</p><div class="table"><a name="idm483208996784"></a><p class="title"><strong>Table 42.1. Registered script tags</strong></p><div class="table-contents"><table class="table" summary="Registered script tags" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Script</th><th>Script Tag</th></tr></thead><tbody><tr><td>Arabic</td><td>arab</td></tr><tr><td>Armenian</td><td>armn</td></tr><tr><td>Bengali</td><td>beng</td></tr><tr><td>Bopomofo</td><td>bopo</td></tr><tr><td>Braille</td><td>brai</td></tr><tr><td>Canadian Syllabics</td><td>cans</td></tr><tr><td>Cherokee</td><td>cher</td></tr><tr><td>Ideographic</td><td>hani</td></tr><tr><td>Default</td><td>DFLT</td></tr><tr><td>Devanagari</td><td>deva</td></tr><tr><td>Ethiopic</td><td>ethi</td></tr><tr><td>Georgian</td><td>geor</td></tr><tr><td>Greek</td><td>grek</td></tr><tr><td>Gujarati</td><td>gujr</td></tr><tr><td>Gurmukhi</td><td>guru</td></tr><tr><td>Hangul Jamo</td><td>jamo</td></tr><tr><td>Hangul</td><td>hang</td></tr><tr><td>Hebrew</td><td>hebr</td></tr><tr><td>Hiragana</td><td>kana</td></tr><tr><td>Kannada</td><td>knda</td></tr><tr><td>Katakana</td><td>kana</td></tr><tr><td>Khmer</td><td>khmr</td></tr><tr><td>Lao</td><td>lao</td></tr><tr><td>Latin</td><td>latn</td></tr><tr><td>Malayalam</td><td>mlym</td></tr><tr><td>Mongolian</td><td>mong</td></tr><tr><td>Myanmar</td><td>mymr</td></tr><tr><td>Ogham</td><td>ogam</td></tr><tr><td>Oriya</td><td>orya</td></tr><tr><td>Runic</td><td>runr</td></tr><tr><td>Sinhala</td><td>sinh</td></tr><tr><td>Syriac</td><td>syrc</td></tr><tr><td>Tamil</td><td>taml</td></tr><tr><td>Telugu</td><td>telu</td></tr><tr><td>Thaana</td><td>thaa</td></tr><tr><td>Thai</td><td>thai</td></tr><tr><td>Tibetan</td><td>tibt</td></tr><tr><td>Yi</td><td>yi</td></tr></tbody></table></div></div><br class="table-break"/><p>When the ScriptList table is searched for a script, and
	  no entry is found, and there is an entry for the 'dflt'
	  script, then this entry must be used. Furthermore, the
	  Script table for the 'dflt' script must have a non-NULL
	  DefaultLangSys and a LangSysCount equal to 0; in other
	  words, there is only a default language for the default
	  script.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm483208947168"></a>Language tags</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.43.3.1"></a>Specification</h4></div></div></div><p>Language system tags identify the language systems
	  supported in a CommonType Layout font. Microsoft uses the
	  standard language system tag names defined in the Windows
	  Natural Language Support API document (called NLSAPI.doc),
	  in Appendix A: Locales and Language ID's. This document is
	  available on the Microsoft Developers Network CD released by
	  Microsoft quarterly, or it can be acquired directly from
	  Microsoft Typography.</p><p>All tags are 4-byte character strings composed of a
	  limited set of ASCII characters in the 0x20-0x7E range. If a
	  language system tag consists of three or less lowercase
	  letters, the letters are followed by the requisite number of
	  spaces (0x20), each consisting of a single byte.</p><div class="table"><a name="idm483208943840"></a><p class="title"><strong>Table 42.2. Registered language tags</strong></p><div class="table-contents"><table class="table" summary="Registered language tags" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Language System Tag</th><th>Language System</th></tr></thead><tbody><tr><td>Abaza</td><td>ABA</td></tr><tr><td>Abkhazian</td><td>ABK</td></tr><tr><td>Adyghe</td><td>ADY</td></tr><tr><td>Afrikaans</td><td>AFK</td></tr><tr><td>Afar</td><td>AFR</td></tr><tr><td>Agaw</td><td>AGW</td></tr><tr><td>Altai</td><td>ALT</td></tr><tr><td>Amharic</td><td>AMH</td></tr><tr><td>Arabic</td><td>ARA</td></tr><tr><td>Aari</td><td>ARI</td></tr><tr><td>Arakanese</td><td>ARK</td></tr><tr><td>Assamese</td><td>ASM</td></tr><tr><td>Athapaskan</td><td>ATH</td></tr><tr><td>Avar</td><td>AVR</td></tr><tr><td>Awadhi</td><td>AWA</td></tr><tr><td>Aymara</td><td>AYM</td></tr><tr><td>Azeri</td><td>AZE</td></tr><tr><td>Badaga</td><td>BAD</td></tr><tr><td>Baghelkhandi</td><td>BAG</td></tr><tr><td>Balkar</td><td>BAL</td></tr><tr><td>Baule</td><td>BAU</td></tr><tr><td>Berber</td><td>BBR</td></tr><tr><td>Bench</td><td>BCH</td></tr><tr><td>Bible Cree</td><td>BCR</td></tr><tr><td>Belarussian</td><td>BEL</td></tr><tr><td>Bemba</td><td>BEM</td></tr><tr><td>Bengali</td><td>BEN</td></tr><tr><td>Bulgarian</td><td>BGR</td></tr><tr><td>Bhili</td><td>BHI</td></tr><tr><td>Bhojpuri</td><td>BHO</td></tr><tr><td>Bikol</td><td>BIK</td></tr><tr><td>Bilen</td><td>BIL</td></tr><tr><td>Blackfoot</td><td>BKF</td></tr><tr><td>Balochi</td><td>BLI</td></tr><tr><td>Balante</td><td>BLN</td></tr><tr><td>Balti</td><td>BLT</td></tr><tr><td>Bambara</td><td>BMB</td></tr><tr><td>Bamileke</td><td>BML</td></tr><tr><td>Breton</td><td>BRE</td></tr><tr><td>Brahui</td><td>BRH</td></tr><tr><td>Braj Bhasha</td><td>BRI</td></tr><tr><td>Burmese</td><td>BRM</td></tr><tr><td>Bashkir</td><td>BSH</td></tr><tr><td>Beti</td><td>BTI</td></tr><tr><td>Catalan</td><td>CAT</td></tr><tr><td>Cebuano</td><td>CEB</td></tr><tr><td>Chechen</td><td>CHE</td></tr><tr><td>Chaha Gurage</td><td>CHG</td></tr><tr><td>Chattisgarhi</td><td>CHH</td></tr><tr><td>Chichewa</td><td>CHI</td></tr><tr><td>Chukchi</td><td>CHK</td></tr><tr><td>Chipewyan</td><td>CHP</td></tr><tr><td>Cherokee</td><td>CHR</td></tr><tr><td>Chuvash</td><td>CHU</td></tr><tr><td>Comorian</td><td>CMR</td></tr><tr><td>Coptic</td><td>COP</td></tr><tr><td>Cree</td><td>CRE</td></tr><tr><td>Carrier</td><td>CRR</td></tr><tr><td>Crimean Tatar</td><td>CRT</td></tr><tr><td>Church Slavonic</td><td>CSL</td></tr><tr><td>Czech</td><td>CSY</td></tr><tr><td>Danish</td><td>DAN</td></tr><tr><td>Dargwa</td><td>DAR</td></tr><tr><td>Woods Cree</td><td>DCR</td></tr><tr><td>German (Standard)</td><td>DEU</td></tr><tr><td>Dogri</td><td>DGR</td></tr><tr><td>Dhivehi</td><td>DHV</td></tr><tr><td>Djerma</td><td>DJR</td></tr><tr><td>Dangme</td><td>DNG</td></tr><tr><td>Dinka</td><td>DNK</td></tr><tr><td>Dungan</td><td>DUN</td></tr><tr><td>Dzongkha</td><td>DZN</td></tr><tr><td>Ebira</td><td>EBI</td></tr><tr><td>Eastern Cree</td><td>ECR</td></tr><tr><td>Edo</td><td>EDO</td></tr><tr><td>Efik</td><td>EFI</td></tr><tr><td>Greek</td><td>ELL</td></tr><tr><td>English</td><td>ENG</td></tr><tr><td>Erzya</td><td>ERZ</td></tr><tr><td>Spanish</td><td>ESP</td></tr><tr><td>Estonian</td><td>ETI</td></tr><tr><td>Basque</td><td>EUQ</td></tr><tr><td>Evenki</td><td>EVK</td></tr><tr><td>Even</td><td>EVN</td></tr><tr><td>Ewe</td><td>EWE</td></tr><tr><td>French Antillean</td><td>FAN</td></tr><tr><td>Farsi</td><td>FAR</td></tr><tr><td>Finnish</td><td>FIN</td></tr><tr><td>Fijian</td><td>FJI</td></tr><tr><td>Flemish</td><td>FLE</td></tr><tr><td>Forest Nenets</td><td>FNE</td></tr><tr><td>Fon</td><td>FON</td></tr><tr><td>Faroese</td><td>FOS</td></tr><tr><td>French (Standard)</td><td>FRA</td></tr><tr><td>Frisian</td><td>FRI</td></tr><tr><td>Friulian</td><td>FRL</td></tr><tr><td>Futa</td><td>FTA</td></tr><tr><td>Fulani</td><td>FUL</td></tr><tr><td>Ga</td><td>GAD</td></tr><tr><td>Gaelic</td><td>GAE</td></tr><tr><td>Gagauz</td><td>GAG</td></tr><tr><td>Galician</td><td>GAL</td></tr><tr><td>Garshuni</td><td>GAR</td></tr><tr><td>Garhwali</td><td>GAW</td></tr><tr><td>Ge'ez</td><td>GEZ</td></tr><tr><td>Gilyak</td><td>GIL</td></tr><tr><td>Gumuz</td><td>GMZ</td></tr><tr><td>Gondi</td><td>GON</td></tr><tr><td>Greenlandic</td><td>GRN</td></tr><tr><td>Garo</td><td>GRO</td></tr><tr><td>Guarani</td><td>GUA</td></tr><tr><td>Gujarati</td><td>GUJ</td></tr><tr><td>Haitian</td><td>HAI</td></tr><tr><td>Halam</td><td>HAL</td></tr><tr><td>Harauti</td><td>HAR</td></tr><tr><td>Hausa</td><td>HAU</td></tr><tr><td>Hawaiin</td><td>HAW</td></tr><tr><td>Hammer-Banna</td><td>HBN</td></tr><tr><td>Hiligaynon</td><td>HIL</td></tr><tr><td>Hindi</td><td>HIN</td></tr><tr><td>High Mari</td><td>HMA</td></tr><tr><td>Hindko</td><td>HND</td></tr><tr><td>Ho</td><td>HO </td></tr><tr><td>Harari</td><td>HRI</td></tr><tr><td>Croatian</td><td>HRV</td></tr><tr><td>Hungarian</td><td>HUN</td></tr><tr><td>Armenian</td><td>HYE</td></tr><tr><td>Igbo</td><td>IBO</td></tr><tr><td>Ijo</td><td>IJO</td></tr><tr><td>Ilokano</td><td>ILO</td></tr><tr><td>Indonesian</td><td>IND</td></tr><tr><td>Ingush</td><td>ING</td></tr><tr><td>Inuktitut</td><td>INU</td></tr><tr><td>Irish</td><td>IRI</td></tr><tr><td>Irish Traditional</td><td>IRT</td></tr><tr><td>Icelandic</td><td>ISL</td></tr><tr><td>Inari Sami</td><td>ISM</td></tr><tr><td>Italian</td><td>ITA</td></tr><tr><td>Hebrew</td><td>IWR</td></tr><tr><td>Javanese</td><td>JAV</td></tr><tr><td>Yiddish</td><td>JII</td></tr><tr><td>Japanese</td><td>JAN</td></tr><tr><td>Judezmo</td><td>JUD</td></tr><tr><td>Jula</td><td>JUL</td></tr><tr><td>Kabardian</td><td>KAB</td></tr><tr><td>Kachchi</td><td>KAC</td></tr><tr><td>Kalenjin</td><td>KAL</td></tr><tr><td>Kannada</td><td>KAN</td></tr><tr><td>Karachay</td><td>KAR</td></tr><tr><td>Georgian</td><td>KAT</td></tr><tr><td>Kazakh</td><td>KAZ</td></tr><tr><td>Kebena</td><td>KEB</td></tr><tr><td>Khutsuri Georgian</td><td>KGE</td></tr><tr><td>Khakass</td><td>KHA</td></tr><tr><td>Khanty-Kazim</td><td>KHK</td></tr><tr><td>Khmer</td><td>KHM</td></tr><tr><td>Khanty-Shurishkar</td><td>KHS</td></tr><tr><td>Khanty-Vakhi</td><td>KHV</td></tr><tr><td>Khowar</td><td>KHW</td></tr><tr><td>Kikuyu</td><td>KIK</td></tr><tr><td>Kirghiz</td><td>KIR</td></tr><tr><td>Kisii</td><td>KIS</td></tr><tr><td>Kokni</td><td>KKN</td></tr><tr><td>Kalmyk</td><td>KLM</td></tr><tr><td>Kamba</td><td>KMB</td></tr><tr><td>Kumaoni</td><td>KMN</td></tr><tr><td>Komo</td><td>KMO</td></tr><tr><td>Komso</td><td>KMS</td></tr><tr><td>Kanuri</td><td>KNR</td></tr><tr><td>Kodagu</td><td>KOD</td></tr><tr><td>Konkani</td><td>KOK</td></tr><tr><td>Kikongo</td><td>KON</td></tr><tr><td>Komi-Permyak</td><td>KOP</td></tr><tr><td>Korean</td><td>KOR</td></tr><tr><td>Komi-Zyrian</td><td>KOZ</td></tr><tr><td>Kpelle</td><td>KPL</td></tr><tr><td>Krio</td><td>KRI</td></tr><tr><td>Karakalpak</td><td>KRK</td></tr><tr><td>Karelian</td><td>KRL</td></tr><tr><td>Karaim</td><td>KRM</td></tr><tr><td>Karen</td><td>KRN</td></tr><tr><td>Koorete</td><td>KRT</td></tr><tr><td>Kashmiri</td><td>KSH</td></tr><tr><td>Khasi</td><td>KSI</td></tr><tr><td>Kildin Sami</td><td>KSM</td></tr><tr><td>Kui</td><td>KUI</td></tr><tr><td>Kulvi</td><td>KUL</td></tr><tr><td>Kumyk</td><td>KUM</td></tr><tr><td>Kurdish</td><td>KUR</td></tr><tr><td>Kurukh</td><td>KUU</td></tr><tr><td>Kuy</td><td>KUY</td></tr><tr><td>Koryak</td><td>KYK</td></tr><tr><td>Ladin</td><td>LAD</td></tr><tr><td>Lahuli</td><td>LAH</td></tr><tr><td>Lak</td><td>LAK</td></tr><tr><td>Lambani</td><td>LAM</td></tr><tr><td>Lao</td><td>LAO</td></tr><tr><td>Latin</td><td>LAT</td></tr><tr><td>Laz</td><td>LAZ</td></tr><tr><td>L-Cree</td><td>LCR</td></tr><tr><td>Ladakhi</td><td>LDK</td></tr><tr><td>Lezgi</td><td>LEZ</td></tr><tr><td>Lingala</td><td>LIN</td></tr><tr><td>Low Mari</td><td>LMA</td></tr><tr><td>Limbu</td><td>LMB</td></tr><tr><td>Lomwe</td><td>LMW</td></tr><tr><td>Lower Sorbian</td><td>LSB</td></tr><tr><td>Lule Sami</td><td>LSM</td></tr><tr><td>Lithuanian</td><td>LTH</td></tr><tr><td>Luba</td><td>LUB</td></tr><tr><td>Luganda</td><td>LUG</td></tr><tr><td>Luhya</td><td>LUH</td></tr><tr><td>Luo</td><td>LUO</td></tr><tr><td>Latvian</td><td>LVI</td></tr><tr><td>Majang</td><td>MAJ</td></tr><tr><td>Makua</td><td>MAK</td></tr><tr><td>Malayalam Traditional</td><td>MAL</td></tr><tr><td>Mansi</td><td>MAN</td></tr><tr><td>Marathi</td><td>MAR</td></tr><tr><td>Marwari</td><td>MAW</td></tr><tr><td>Mbundu</td><td>MBN</td></tr><tr><td>Manchu</td><td>MCH</td></tr><tr><td>Moose Cree</td><td>MCR</td></tr><tr><td>Mende</td><td>MDE</td></tr><tr><td>Me'en</td><td>MEN</td></tr><tr><td>Mizo</td><td>MIZ</td></tr><tr><td>Macedonian</td><td>MKD</td></tr><tr><td>Male</td><td>MLE</td></tr><tr><td>Malagasy</td><td>MLG</td></tr><tr><td>Malinke</td><td>MLN</td></tr><tr><td>Malayalam Reformed</td><td>MLR</td></tr><tr><td>Malay</td><td>MLY</td></tr><tr><td>Mandinka</td><td>MND</td></tr><tr><td>Mongolian</td><td>MNG</td></tr><tr><td>Manipuri</td><td>MNI</td></tr><tr><td>Maninka</td><td>MNK</td></tr><tr><td>Manx Gaelic</td><td>MNX</td></tr><tr><td>Moksha</td><td>MOK</td></tr><tr><td>Moldavian</td><td>MOL</td></tr><tr><td>Mon</td><td>MON</td></tr><tr><td>Moroccan</td><td>MOR</td></tr><tr><td>Maori</td><td>MRI</td></tr><tr><td>Maithili</td><td>MTH</td></tr><tr><td>Maltese</td><td>MTS</td></tr><tr><td>Mundari</td><td>MUN</td></tr><tr><td>Naga-Assamese</td><td>NAG</td></tr><tr><td>Nanai</td><td>NAN</td></tr><tr><td>Naskapi</td><td>NAS</td></tr><tr><td>N-Cree</td><td>NCR</td></tr><tr><td>Ndebele</td><td>NDB</td></tr><tr><td>Ndonga</td><td>NDG</td></tr><tr><td>Nepali</td><td>NEP</td></tr><tr><td>Newari</td><td>NEW</td></tr><tr><td>Norway House Cree</td><td>NHC</td></tr><tr><td>Nisi</td><td>NIS</td></tr><tr><td>Niuean</td><td>NIU</td></tr><tr><td>Nkole</td><td>NKL</td></tr><tr><td>Dutch</td><td>NLD</td></tr><tr><td>Nogai</td><td>NOG</td></tr><tr><td>Norwegian</td><td>NOR</td></tr><tr><td>Northern Sami</td><td>NSM</td></tr><tr><td>Northern Tai</td><td>NTA</td></tr><tr><td>Esperanto</td><td>NTO</td></tr><tr><td>Nynorsk</td><td>NYN</td></tr><tr><td>Oji-Cree</td><td>OCR</td></tr><tr><td>Ojibway</td><td>OJB</td></tr><tr><td>Oriya</td><td>ORI</td></tr><tr><td>Oromo</td><td>ORO</td></tr><tr><td>Ossetian</td><td>OSS</td></tr><tr><td>Palestinian Aramaic</td><td>PAA</td></tr><tr><td>Pali</td><td>PAL</td></tr><tr><td>Punjabi</td><td>PAN</td></tr><tr><td>Palpa</td><td>PAP</td></tr><tr><td>Pashto</td><td>PAS</td></tr><tr><td>Polytonic Greek</td><td>PGR</td></tr><tr><td>Pilipino</td><td>PIL</td></tr><tr><td>Palaung</td><td>PLG</td></tr><tr><td>Polish</td><td>PLK</td></tr><tr><td>Provencal</td><td>PRO</td></tr><tr><td>Portuguese</td><td>PTG</td></tr><tr><td>Chin</td><td>QIN</td></tr><tr><td>Rajasthani</td><td>RAJ</td></tr><tr><td>R-Cree</td><td>RCR</td></tr><tr><td>Russian Buriat</td><td>RBU</td></tr><tr><td>Riang</td><td>RIA</td></tr><tr><td>Rhaeto-Romanic</td><td>RMS</td></tr><tr><td>Romanian</td><td>ROM</td></tr><tr><td>Romany</td><td>ROY</td></tr><tr><td>Rusyn</td><td>RSY</td></tr><tr><td>Ruanda</td><td>RUA</td></tr><tr><td>Russian</td><td>RUS</td></tr><tr><td>Sadri</td><td>SAD</td></tr><tr><td>Sanskrit</td><td>SAN</td></tr><tr><td>Santali</td><td>SAT</td></tr><tr><td>Sayisi</td><td>SAY</td></tr><tr><td>Sekota</td><td>SEK</td></tr><tr><td>Selkup</td><td>SEL</td></tr><tr><td>Sango</td><td>SGO</td></tr><tr><td>Shan</td><td>SHN</td></tr><tr><td>Sibe</td><td>SIB</td></tr><tr><td>Sidamo</td><td>SID</td></tr><tr><td>Silte Gurage</td><td>SIG</td></tr><tr><td>Skolt Sami</td><td>SKS</td></tr><tr><td>Slovak</td><td>SKY</td></tr><tr><td>Slavey</td><td>SLA</td></tr><tr><td>Slovenian</td><td>SLV</td></tr><tr><td>Somali</td><td>SML</td></tr><tr><td>Samoan</td><td>SMO</td></tr><tr><td>Sena</td><td>SNA</td></tr><tr><td>Sindhi</td><td>SND</td></tr><tr><td>Sinhalese</td><td>SNH</td></tr><tr><td>Soninke</td><td>SNK</td></tr><tr><td>Sodo Gurage</td><td>SOG</td></tr><tr><td>Sotho</td><td>SOT</td></tr><tr><td>Albanian</td><td>SQI</td></tr><tr><td>Serbian</td><td>SRB</td></tr><tr><td>Saraiki</td><td>SRK</td></tr><tr><td>Serer</td><td>SRR</td></tr><tr><td>South Slavey</td><td>SSL</td></tr><tr><td>Southern Sami</td><td>SSM</td></tr><tr><td>Suri</td><td>SUR</td></tr><tr><td>Svan</td><td>SVA</td></tr><tr><td>Swedish</td><td>SVE</td></tr><tr><td>Swadaya Aramaic</td><td>SWA</td></tr><tr><td>Swahili</td><td>SWK</td></tr><tr><td>Swazi</td><td>SWZ</td></tr><tr><td>Sutu</td><td>SXT</td></tr><tr><td>Syriac</td><td>SYR</td></tr><tr><td>Tabasaran</td><td>TAB</td></tr><tr><td>Tajiki</td><td>TAJ</td></tr><tr><td>Tamil</td><td>TAM</td></tr><tr><td>Tatar</td><td>TAT</td></tr><tr><td>TH-Cree</td><td>TCR</td></tr><tr><td>Telugu</td><td>TEL</td></tr><tr><td>Tongan</td><td>TGN</td></tr><tr><td>Tigre</td><td>TGR</td></tr><tr><td>Tigrinya</td><td>TGY</td></tr><tr><td>Thai</td><td>THA</td></tr><tr><td>Tahitian</td><td>THT</td></tr><tr><td>Tibetan</td><td>TIB</td></tr><tr><td>Turkmen</td><td>TKM</td></tr><tr><td>Temne</td><td>TMN</td></tr><tr><td>Tswana</td><td>TNA</td></tr><tr><td>Tundra Nenets</td><td>TNE</td></tr><tr><td>Tonga</td><td>TNG</td></tr><tr><td>Todo</td><td>TOD</td></tr><tr><td>Turkish</td><td>TRK</td></tr><tr><td>Tsonga</td><td>TSG</td></tr><tr><td>Turoyo Aramaic</td><td>TUA</td></tr><tr><td>Tulu</td><td>TUL</td></tr><tr><td>Tuvin</td><td>TUV</td></tr><tr><td>Twi</td><td>TWI</td></tr><tr><td>Udmurt</td><td>UDM</td></tr><tr><td>Ukrainian</td><td>UKR</td></tr><tr><td>Urdu</td><td>URD</td></tr><tr><td>Upper Sorbian</td><td>USB</td></tr><tr><td>Uyghur</td><td>UYG</td></tr><tr><td>Uzbek</td><td>UZB</td></tr><tr><td>Venda</td><td>VEN</td></tr><tr><td>Vietnamese</td><td>VIT</td></tr><tr><td>Wa</td><td>WA </td></tr><tr><td>Wagdi</td><td>WAG</td></tr><tr><td>West-Cree</td><td>WCR</td></tr><tr><td>Welsh</td><td>WEL</td></tr><tr><td>Wolof</td><td>WLF</td></tr><tr><td>Xhosa</td><td>XHS</td></tr><tr><td>Yakut</td><td>YAK</td></tr><tr><td>Yoruba</td><td>YBA</td></tr><tr><td>Y-Cree</td><td>YCR</td></tr><tr><td>Yi Classic</td><td>YIC</td></tr><tr><td>Yi Modern</td><td>YIM</td></tr><tr><td>Chinese Phonetic</td><td>ZHP</td></tr><tr><td>Chinese Simplified</td><td>ZHS</td></tr><tr><td>Chinese Traditional</td><td>ZHT</td></tr><tr><td>Zande</td><td>ZND</td></tr><tr><td>Zulu</td><td>ZUL</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm483208478016"></a>Baseline tags</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.43.4.1"></a>Specification</h4></div></div></div><p>This section defines the standard CommonType Layout
	  baseline tags that Microsoft supports. A registered baseline
	  tag has a specific meaning when used in the horizontal
	  writing direction (used in the <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table's HorizAxis
	  table), vertical writing direction (used in the <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a>
	  table's VertAxis table), or both, and conveys information to
	  font users about a baseline's use. For example, the "romn"
	  baseline tag is commonly used to identify the baseline to
	  layout Latin text in the horizontal, vertical, or both
	  directions for Latin text layout. For compatibility and ease
	  of use, Microsoft encourages font developers to use
	  registered baseline tags.</p><p>This version of the Tag Registry identifies the
	  baselines that Microsoft has implemented to date. All
	  baseline tags are 4-byte character strings composed of a
	  limited set of ASCII characters in the 0x20-0x7E
	  range. Baseline tags consist of four lowercase
	  letters. </p><div class="table"><a name="idm483208473168"></a><p class="title"><strong>Table 42.3. Registered baseline tags</strong></p><div class="table-contents"><table class="table" summary="Registered baseline tags" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Baseline Tag</th><th>Baseline for HorizAxis</th><th>Baseline for VertAxis</th></tr></thead><tbody><tr><td>hang</td><td>The hanging baseline. This is the horizontal
		  line from which syllables seem to hang in Tibetan
		script.</td><td>The hanging baseline, (which now appears
		vertical) for Tibetan characters rotated 90 degrees
		clockwise, for vertical writing mode.</td></tr><tr><td>icfb</td><td>deographic character face bottom edge
		baseline. (See section Ideographic Character Face
		below for usage.)</td><td>Ideographic character
		face left edge baseline.  (See section Ideographic
		Character Face below for usage.)</td></tr><tr><td>icft</td><td>Ideographic character face
		top edge baseline.  (See section Ideographic Character
		Face below for usage.)</td><td>Ideographic
		character face right edge baseline.  (See section
		Ideographic Character Face below for usage.)</td></tr><tr><td>ideo</td><td>Ideographic em-box bottom
		edge baseline.  (See section Ideographic Em-Box below
		for usage.)</td><td>Ideographic em-box left
		edge baseline. If this tag is present in the VertAxis,
		the value must be set to 0.  (See section Ideographic
		Em-Box below for usage.)</td></tr><tr><td>idtp</td><td>Ideographic em-box top edge
		baseline. (See section Ideographic Em-Box below for
		usage.)</td><td>Ideographic em-box right edge
		baseline. If this tag is present in the VertAxis, the
		value is strongly recommended to be set to
		head.unitsPerEm. (See section Ideographic Em-Box below
		for usage.)</td></tr><tr><td>math</td><td>The baseline about which
		mathematical characters are centered.</td><td>The baseline about which mathematical
		characters, when rotated 90 degrees clockwise for
		vertical writing mode, are centered.</td></tr><tr><td>romn</td><td>The baseline used by simple
		alphabetic scripts such as Latin, Cyrillic and
		Greek.</td><td>The alphabetic baseline for
		characters rotated 90 degrees clockwise for vertical
		writing mode. (This would not apply to alphabetic
		characters that remain upright in vertical writing
		mode, since these characters are not rotated.)</td></tr></tbody></table></div></div><br class="table-break"/><h5><a name="idm483208456672"></a>Ideographic Em-Box</h5><p>The notation &lt;Axis&gt;.&lt;Baseline Tag&gt; is used in the
	  following description to mean the baseline tag as defined in
	  the specified axis. For example, HorizAxis.ideo means the
	  ideo baseline tag as defined in the HorizAxis of the BASE
	  table. See above for a list of registered baseline
	  tags.</p><p>A font’s ideographic em-box is the rectangle that
	  defines a standard escapement around the full-width
	  ideographic glyphs of the font, for both the horizontal and
	  vertical writing directions. It is usually a square, but may
	  be non-square as in the case of fonts used in Japanese
	  newspaper layout that have a vertically condensed
	  design.</p><p>The left, right, top and bottom edges of the ideographic
	  em-box are to be determined as follows:</p><div class="literallayout"><p><br/>
ideoEmboxLeft = 0<br/>
<br/>
If HorizAxis.ideo defined:<br/>
<br/>
    ideoEmboxBottom = HorizAxis.ideo<br/>
<br/>
    If HorizAxis.idtp defined:<br/>
        ideoEmboxTop = HorizAxis.idtp<br/>
    Else:<br/>
        ideoEmboxTop = HorizAxis.ideo + head.unitsPerEm<br/>
<br/>
    If VertAxis.idtp defined:<br/>
        ideoEmboxRight = VertAxis.idtp<br/>
    Else:<br/>
        ideoEmboxRight = head.unitsPerEm<br/>
<br/>
    If VertAxis.ideo defined and non-zero:<br/>
        Warning: Bad VertAxis.ideo value<br/>
<br/>
Else If this is a CJK font:<br/>
<br/>
    ideoEmboxBottom = OS/2.sTypoDescender<br/>
    ideoEmboxTop = OS/2.sTypoAscender<br/>
    ideoEmboxRight = head.unitsPerEm<br/>
<br/>
Else:<br/>
    ideoEmbox cannot be determined for this font<br/>
</p></div><p>Determining whether a font is CJK (Chinese, Japanese, or
	  Korean) or not, as in the second-last "Else" clause above,
	  can be done by checking the CJK-related bits of the
	  OS/2.ulUnicodeRange fields.</p><p>Note that font designers can specify a HorizAxis.ideo
	  baseline in their non-CJK fonts; this can be used by
	  applications when aligning the font with an ideographic font
	  used on the same line of text, when the user has specified
	  ideographic em-box alignment.</p><p>The ideographic em-box center baseline is defined as
	  halfway between the ideographic em-box top and bottom
	  baselines in the horizontal axis, and halfway between the
	  ideographic em-box left and right baselines in the vertical
	  axis. These center baselines are defined in whole character
	  units. The division used in the calculation must round to
	  the character unit nearest 0 if needed. Thus, for maximal
	  precision of center baseline placement, vendors should
	  ensure that opposite edges of the ideographic em-box box are
	  an even number of character units apart.</p><p>Example:</p><p>The values of the ideographic baseline tags for the
	  Kozuka Mincho font family (designed on a 1000-unit em) are:
	  HorizAxis.ideo = -120; HorizAxis.idtp = 880. Since this
	  describes a square ideographic em-box, it is sufficient to
	  record only the following: HorizAxis.ideo = -120. If
	  HorizAxis.ideo is not present, then the following will be
	  used for the ideographic em-box bottom and top, since this
	  is a CJK font: OS/2.sTypoDescender = -120;
	  OS/2.sTypoAscender = 880.</p><p>Compatibility notes:

	  </p><div class="orderedlist"><ol class="orderedlist" type="1"><li class="listitem"><p>Most applications expect the width of full-width
	      ideographs in a CJK font to be exactly one em, thus it
	      is strongly recommended that VertAxis.idtp, if present,
	      be set to head.unitsPerEm. (The idtp baseline tag was
	      introduced in CommonType 1.3.)</p></li><li class="listitem"><p>While the CommonType specification allows for CJK
		fonts' OS/2.sTypoDescender and OS/2.sTypoAscender
		fields to specify metrics different from the
		HorizAxis.ideo and HorizAxis.idtp in the <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table,
		CJK font developers should be aware that existing
		applications may not read the <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table at all but
		simply use the OS/2.sTypoDescender and
		OS/2.sTypoAscender fields to describe the bottom and
		top edges of the ideographic em-box. If developers
		want their fonts to work correctly with such
		applications, they should ensure that any ideographic
		em-box values in the <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table of their CJK fonts
		describe the same bottom and top edges as the
		OS/2.sTypoDescender and OS/2.sTypoAscender fields.</p></li><li class="listitem"><p>Applications on platforms other than Windows that
	      don't parse the <a class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table won't have
	      access to the OS/2.sTypoDescender and OS/2.sTypoAscender
	      fields, since these metrics are exposed only through
	      Windows APIs currently. Thus, CJK fonts will typically
	      have the same descender value recorded in
	      hhea.Descender, OS/2.sTypoDescender, and HorizAxis.ideo
	      (if present), and the same Ascender value recorded in
	      hhea.Ascender, OS/2.sTypoAscender, and HorizAxis.idtp
	      (if present).</p></li></ol></div><p>
      </p><p>See the section "CommonType CJK Font Guidelines"
	    for more information about constructing CJK
	    fonts.</p><h5><a name="idm483208441408"></a>Ideographic Character Face</h5><p>he notation &lt;Axis&gt;.&lt;Baseline Tag&gt; is used in the
	  following description to mean the baseline tag as defined in
	  the specified axis. For example, HorizAxis.icfb means the
	  icfb baseline tag as defined in the HorizAxis of the BASE
	  table. See above for a list of registered baseline
	  tags.</p><p>The ideographic character face (ICF), also known as the
	average character face (ACF), specifies the approximate
	bounding box of the full-width ideographic and kana glyphs in
	a CJK font. (This is different from the FontBBox, as described
	in the PostScript programming language, which is the bounding
	box of all glyphs in the font.) In Japanese, the term for ICF
	is heikin jizura.</p><p>It is typically expressed as a percentage that
	represents the ratio of the length of an ICF box edge to the
	length of an ideographic em-box edge, and is conceptualized as
	a square centered within the ideographic em-box. However, in
	CommonType, the ICF box's left, bottom, right, and top edges are
	specified as the VertAxis.icfb, HorizAxis.icfb, VertAxis.icft,
	and HorizAxis.icft baselines, respectively, thus giving font
	designers the flexibility to specify a non-square and/or
	non-centered ICF box.</p><p>Font designers should set the value of the ICF box edges
	based on how tight or loose they want the font to appear when
	text is set with no tracking or kerning (beta gumi in
	Japanese). Therefore, the left-over boundary of the
	ideographic em-box around the ICF box is the default
	escapement of the font.</p><p>Applications can use the ICF box as an alignment tool,
	to ensure that glyphs touch the edges of the text frame and
	page objects are visually aligned to text edges. It is also
	useful for aligning glyphs of different sizes on the same
	line. In Japanese traditional paper-based workflow, the ICF
	box was often used for these purposes. It provides optically
	aligned results that are superior to using the ideographic
	em-box.</p><p>HorizAxis.icfb is the mininum piece of information
	required to define the ICF, in a CJK font. First, the
	ideographic em-box dimensions must be calculated as in the
	section "Ideographic Em-Box" above. The ICF edges are then
	calculated in the following order:</p><div class="literallayout"><p><br/>
<br/>
If HorizAxis.icfb defined:<br/>
<br/>
    icfBottom = HorizAxis.icfb<br/>
    margin = HorizAxis.icfb - ideoEmboxBottom<br/>
<br/>
    If HorizAxis.icft defined:<br/>
      icfTop = HorizAxis.icft<br/>
    Else:<br/>
      icfTop = ideoEmboxTop - margin<br/>
<br/>
    If VertAxis.icfb defined:<br/>
      icfLeft = VertAxis.icfb<br/>
    Else:<br/>
      icfLeft = margin<br/>
<br/>
    If VertAxis.icft defined:<br/>
      icfRight = VertAxis.icft<br/>
    Else:<br/>
      icfRight = ideoEmBoxRight - icfLeft<br/>
<br/>
Else:<br/>
   ICF cannot be determined for this font<br/>
</p></div><p>For the last case above, i.e. fonts that don't have ICF
	  information in their <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table, an
	  application may choose to apply a heuristic such as
	  calculating the bounding box of some or all of the
	  ideographic and kana glyphs, and then averaging its margin
	  with the ideographic em-box.</p><p>The ICF center baseline is defined as halfway between
	the ICF top and bottom baselines in the horizontal axis, and
	halfway between the ICF left and right baselines in the
	vertical axis. These center baselines are defined in whole
	character units. The division used in the calculation must
	round to the character unit nearest 0 if needed. Thus, for
	maximal precision of center baseline placement, vendors should
	ensure that opposite edges of the ICF box are an even number
	of character units apart.</p><p>Example:</p><p>The values of the ICF baselines for the Extra Light and
	Heavy weights of the Kozuka Mincho font family (designed on a
	1000-unit em, with ideographic em-box as given in the example
	in the previous section) are:</p><div class="literallayout"><p><br/>
    Kozuka Mincho Extra Light:<br/>
    VertAxis.icfb = 41; HorizAxis.icfb = -79;<br/>
    VertAxis.icft = 959; HorizAxis.icft = 839.<br/>
</p></div><p>Since this describes a square ICF centered in a square
	ideographic em-box, it is sufficient to record only the
	following:</p><div class="literallayout"><p><br/>
    HorizAxis.icfb = -79.<br/>
</p></div><div class="literallayout"><p><br/>
    Kozuka Mincho Heavy:<br/>
    VertAxis.icfb = 26; HorizAxis.icfb = -94;<br/>
    VertAxis.icft = 974; HorizAxis.icft = 854.<br/>
</p></div><p>It is sufficient to record only:</p><div class="literallayout"><p><br/>
HorizAxis.icfb = -94.<br/>
</p></div><p>It is strongly recommended that each of the edges of the
	ICF box be equidistant from the corresponding edge of the
	ideographic em-box. Following this will result in more
	predictable results in applications that use these
	values. That is, for fonts based on a square ideographic
	em-box, the ICF box should be a centered square.</p><p>See the section "CommonType CJK Font Guidelines" for more
	  information about constructing CJK fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm483208427376"></a>Feature tags</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.43.5.1"></a>Specification</h4></div></div></div><p>Features provide information about how to use the glyphs
	in a font to render a script or language. For example, an
	Arabic font might have a feature for substituting initial
	glyph forms, and a Kanji font might have a feature for
	positioning glyphs vertically. All CommonType Layout features
	define data for glyph substitution, glyph positioning, or
	both.</p><p>Each CommonType Layout feature has a feature tag that
	identifies its typographic function and effects. By examining
	a feature's tag, a text-processing client can determine what a
	feature does and decide whether to implement it. All tags are
	4-byte character strings composed of a limited set of ASCII
	characters in the 0x20-0x7E range. Microsoft-registered
	feature tags use four lowercase letters. For instance, the
	"mark" feature manages the placement of diacritical marks, and
	the "swsh" feature renders swash glyphs.</p><p>A feature definition may not provide all the information
	required to properly implement glyph substitution or
	positioning actions. In many cases, a text-processing client
	may need to supply additional data. For example, the function
	of the "init" feature is to provide initial glyph
	forms. Nothing in the feature's lookup tables indicates when
	or where to apply this feature during text processing. To
	correctly use the "init" feature in Arabic text where initial
	glyph forms appear at the beginning of words, text-processing
	clients must be able to identify the first glyph position in
	each word before making the glyph substitution. In all cases,
	the text-processing client is responsible for applying,
	combining, and arbitrating among features and rendering the
	result.</p><p>The tag space defined by tags consisting of four
	uppercase letters (A-Z) with no punctuation, spaces, or
	numbers, is reserved as a vendor space. Font vendors may use
	such tags to identify private features. For example, the
	feature tag "PKRN" might designate a private feature that may
	be used to kern punctuation marks. Microsoft does not
	guarantee the compatibility or usability of private features,
	and it cannot ensure that two font vendors will not choose the
	same tag for a private feature.</p><p>This version of the Tag Registry describes all the
	CommonType Layout features Microsoft has developed to date. It
	also includes details that identify the lookups that Microsoft
	uses to implement each feature. Lookup information is provided
	for reference purposes only; the set of lookups used to
	implement a feature will vary across system platforms,
	applications, fonts, and font developers.</p><h5><a name="idm483208421040"></a>To register features</h5><p>Microsoft encourages font developers to use 'registered'
	feature tags when implementing registered features. However,
	font developers also may define and register their own
	features.</p><p>Microsoft welcomes nominations for new features and
	feature tags to register. To qualify for registration, a
	feature must have a single function that is clearly identified
	by its tag. The function of the feature should be defined at
	the lowest useful level and must be distinctly different from
	the functions of currently registered features. When font
	developers register feature tags and functions with Microsoft,
	they do not have to supply implementation details.</p><p>Microsoft reserves the right to officially assign
	feature tags in the Microsoft Tag Registry. Although Microsoft
	has reserved the feature and feature tag definitions listed in
	this registry, Microsoft fonts do not necessarily contain all
	of the features.</p><h5><a name="idm483208418528"></a>Registered features</h5><p>The features listed below are sorted in alphabetical
	order by tag name. Click on the feature tag to view feature
	description and implementation, or go to the feature
	descriptions page.</p><div class="table"><a name="idm483208417536"></a><p class="title"><strong>Table 42.4. List of registered features</strong></p><div class="table-contents"><table class="table" summary="List of registered features" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Feature Tag</th><th>Friendly Name</th></tr></thead><tbody><tr><td>aalt</td><td>Access All Alternates</td></tr><tr><td>abvf</td><td>Above-base Forms</td></tr><tr><td>abvm</td><td>Above-base Mark Positioning</td></tr><tr><td>abvs</td><td>Above-base Substitutions</td></tr><tr><td>afrc</td><td>Alternative Fractions</td></tr><tr><td>akhn</td><td>Akhands</td></tr><tr><td>blwf</td><td>Below-base Forms</td></tr><tr><td>blwm</td><td>Below-base Mark Positioning</td></tr><tr><td>blws</td><td>Below-base Substitutions</td></tr><tr><td>calt</td><td>Contextual Alternates</td></tr><tr><td>case</td><td>Case-Sensitive Forms</td></tr><tr><td>ccmp</td><td>Glyph Composition / Decomposition</td></tr><tr><td>clig</td><td>Contextual Ligatures</td></tr><tr><td>cpsp</td><td>Capital Spacing</td></tr><tr><td>cswh</td><td>Contextual Swash</td></tr><tr><td>curs</td><td>Cursive Positioning</td></tr><tr><td>c2sc</td><td>Small Capitals From Capitals</td></tr><tr><td>c2pc</td><td>Petite Capitals From Capitals</td></tr><tr><td>dist</td><td>Distances</td></tr><tr><td>dlig</td><td>Discretionary Ligatures</td></tr><tr><td>dnom</td><td>Denominators</td></tr><tr><td>expt</td><td>Expert Forms</td></tr><tr><td>falt</td><td>Final Glyph on Line Alternates</td></tr><tr><td>fin2</td><td>Terminal Forms #2</td></tr><tr><td>fin3</td><td>Terminal Forms #3</td></tr><tr><td>fina</td><td>Terminal Forms</td></tr><tr><td>frac</td><td>Fractions</td></tr><tr><td>fwid</td><td>Full Widths</td></tr><tr><td>half</td><td>Half Forms</td></tr><tr><td>haln</td><td>Halant Forms</td></tr><tr><td>halt</td><td>Alternate Half Widths</td></tr><tr><td>hist</td><td>Historical Forms</td></tr><tr><td>hkna</td><td>Horizontal Kana Alternates</td></tr><tr><td>hlig</td><td>Historical Ligatures</td></tr><tr><td>hngl</td><td>Hangul</td></tr><tr><td>hwid</td><td>Half Widths</td></tr><tr><td>init</td><td>Initial Forms</td></tr><tr><td>isol</td><td>Isolated Forms</td></tr><tr><td>ital</td><td>Italics</td></tr><tr><td>jalt</td><td>Justification Alternates</td></tr><tr><td>jp78</td><td>JIS78 Forms</td></tr><tr><td>jp83</td><td>JIS83 Forms</td></tr><tr><td>jp90</td><td>JIS90 Forms</td></tr><tr><td>kern</td><td>Kerning</td></tr><tr><td>lfbd</td><td>Left Bounds</td></tr><tr><td>liga</td><td>Standard Ligatures</td></tr><tr><td>ljmo</td><td>Leading Jamo Forms</td></tr><tr><td>lnum</td><td>Lining Figures</td></tr><tr><td>locl</td><td>Localized Forms</td></tr><tr><td>mark</td><td>Mark Positioning</td></tr><tr><td>med2</td><td>Medial Forms #2</td></tr><tr><td>medi</td><td>Medial Forms</td></tr><tr><td>mgrk</td><td>Mathematical Greek</td></tr><tr><td>mkmk</td><td>Mark to Mark Positioning</td></tr><tr><td>mset</td><td>Mark Positioning via Substitution</td></tr><tr><td>nalt</td><td>Alternate Annotation Forms</td></tr><tr><td>nlck</td><td>NLC Kanji Forms</td></tr><tr><td>nukt</td><td>Nukta Forms</td></tr><tr><td>numr</td><td>Numerators</td></tr><tr><td>onum</td><td>Oldstyle Figures</td></tr><tr><td>opbd</td><td>Optical Bounds</td></tr><tr><td>ordn</td><td>Ordinals</td></tr><tr><td>ornm</td><td>Ornaments</td></tr><tr><td>palt</td><td>Proportional Alternate Widths</td></tr><tr><td>pcap</td><td>Petite Capitals</td></tr><tr><td>pnum</td><td>Proportional Figures</td></tr><tr><td>pref</td><td>Pre-Base Forms</td></tr><tr><td>pres</td><td>Pre-base Substitutions</td></tr><tr><td>pstf</td><td>Post-base Forms</td></tr><tr><td>psts</td><td>Post-base Substitutions</td></tr><tr><td>pwid</td><td>Proportional Widths</td></tr><tr><td>qwid</td><td>Quarter Widths</td></tr><tr><td>rand</td><td>Randomize</td></tr><tr><td>rlig</td><td>Required Ligatures</td></tr><tr><td>rphf</td><td>Reph Forms</td></tr><tr><td>rtbd</td><td>Right Bounds</td></tr><tr><td>rtla</td><td>Right-to-left alternates</td></tr><tr><td>ruby</td><td>Ruby Notation Forms</td></tr><tr><td>salt</td><td>Stylistic Alternates</td></tr><tr><td>sinf</td><td>Scientific Inferiors</td></tr><tr><td>size</td><td>Optical size</td></tr><tr><td>smcp</td><td>Small Capitals</td></tr><tr><td>smpl</td><td>Simplified Forms</td></tr><tr><td>ss01</td><td>Stylistic Set 1</td></tr><tr><td>ss02</td><td>Stylistic Set 2</td></tr><tr><td>ss03</td><td>Stylistic Set 3</td></tr><tr><td>ss04</td><td>Stylistic Set 4</td></tr><tr><td>ss05</td><td>Stylistic Set 5</td></tr><tr><td>ss06</td><td>Stylistic Set 6</td></tr><tr><td>ss07</td><td>Stylistic Set 7</td></tr><tr><td>ss08</td><td>Stylistic Set 8</td></tr><tr><td>ss09</td><td>Stylistic Set 9</td></tr><tr><td>ss10</td><td>Stylistic Set 10</td></tr><tr><td>ss11</td><td>Stylistic Set 11</td></tr><tr><td>ss12</td><td>Stylistic Set 12</td></tr><tr><td>ss13</td><td>Stylistic Set 13</td></tr><tr><td>ss14</td><td>Stylistic Set 14</td></tr><tr><td>ss15</td><td>Stylistic Set 15</td></tr><tr><td>ss16</td><td>Stylistic Set 16</td></tr><tr><td>ss17</td><td>Stylistic Set 17</td></tr><tr><td>ss18</td><td>Stylistic Set 18</td></tr><tr><td>ss19</td><td>Stylistic Set 19</td></tr><tr><td>ss20</td><td>Stylistic Set 20</td></tr><tr><td>subs</td><td>Subscript</td></tr><tr><td>sups</td><td>Superscript</td></tr><tr><td>swsh</td><td>Swash</td></tr><tr><td>titl</td><td>Titling</td></tr><tr><td>tjmo</td><td>Trailing Jamo Forms</td></tr><tr><td>tnam</td><td>Traditional Name Forms</td></tr><tr><td>tnum</td><td>Tabular Figures</td></tr><tr><td>trad</td><td>Traditional Forms</td></tr><tr><td>twid</td><td>Third Widths</td></tr><tr><td>unic</td><td>Unicase</td></tr><tr><td>valt</td><td>Alternate Vertical Metrics</td></tr><tr><td>vatu</td><td>Vattu Variants</td></tr><tr><td>vert</td><td>Vertical Writing</td></tr><tr><td>vhal</td><td>Alternate Vertical Half Metrics</td></tr><tr><td>vjmo</td><td>Vowel Jamo Forms</td></tr><tr><td>vkna</td><td>Vertical Kana Alternates</td></tr><tr><td>vkrn</td><td>Vertical Kerning</td></tr><tr><td>vpal</td><td>Proportional Alternate Vertical Metrics</td></tr><tr><td>vrt2</td><td>Vertical Alternates and Rotation</td></tr><tr><td>zero</td><td>Slashed Zero</td></tr></tbody></table></div></div><br class="table-break"/><p>Tag: 'aalt'</p><p>Friendly name: Access All Alternates</p><p>Registered by: Adobe</p><p>Function: This feature makes all variations of a
	selected character accessible. This serves several purposes:
	An application may not support the feature by which the
	desired glyph would normally be accessed; the user may need a
	glyph outside the context supported by the normal
	substitution, or the user may not know what feature produces
	the desired glyph. Since many-to-one substitutions are not
	covered, ligatures would not appear in this table unless they
	were variant forms of another ligature.</p><p>Example: A user inputs the P in Poetica, and is
	presented with a choice of the four standard capital forms,
	the eight swash capital forms, the initial capital form and
	the small capital form.</p><p>Recommended implementation: The aalt table groups glyphs
	into semantic units. These units include the glyph which
	represents the default form for the underlying Unicode value
	stored by the application. While many of these substitutions
	are one-to-one (GSUB lookup type 1), others require a
	selection from a set (GSUB lookup type 3). The manufacturer
	may choose to build two tables (one for each lookup type) or
	only one which uses lookup type 3 for all substitutions. As in
	any one-from-many substitution, alternates present in more
	than one face should be ordered consistently across a family,
	so that those alternates can work correctly when switching
	between family members. This feature should be ordered first
	in the font, to take precedence over other features.</p><p>Application interface: The application determines the
	GID for the default form of a given character (Unicode value
	with no features applied). It then checks to see whether the
	GID is found in the aalt coverage table. If so, the
	application passes this value to the feature table and gets
	back the GIDs in the associated group.</p><p>UI suggestion: While most one-from-many substitution
	features can be applied globally with reasonable results, aalt
	i not designed to support this use. The application should
	indicate to the user which glyphs in the user's document have
	alternative forms (i.e which are in the coverage table for
	aalt). When the user selects one of those glyphs and applies
	the aalt feature, an application could display the forms
	sequentially in context, or present a palette showing all the
	forms at once, or give the user a choice between these
	approaches. The application may assume that the first glyph in
	a set is the preferred form, so the font developer should
	order them accordingly. When only one alternate exists, this
	feature could toggle directly between the alternate and
	default forms.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may be used in
	combination with other features.</p><p>Tag: 'abvf'</p><p>Friendly name: Above-base Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the above-base form of a vowel.</p><p>Example: In complex scripts like Khmer, the vowel OE
	must be split into a pre-base form and an above-base form. The
	above-base form of OE would be substituted to form the correct
	piece of the letter that is displayed above the base
	consonant.</p><p>Recommended implementation: This feature substitutes the
	GID for OE with the above part of the glyph (GSUB lookup type
	1).</p><p>Application interface: In a sequence where a split vowel
	with an above form is used, the application must insert the
	pre-base glyph into the correct location and then apply the
	above-base form feature. The application gets back the GID for
	the correct form for the piece that is placed above the base
	glyph. The application may also choose to position this glyph
	if required, after this feature is called.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Khmer script.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'abvm'</p><p>Friendly name: Above-base Mark Positioning</p><p>Registered by: Microsoft</p><p>Function: Positions marks above base glyphs.</p><p>Example: In complex scripts like Devanagari (Indic), the
	Anuswar needs to be positioned above the base glyph. This base
	glyph can be a base consonant or conjunct. The base glyph and
	the presence/absence of other marks above the base glyph
	decides the location of the Anuswar, so that they do not
	overlap each other.</p><p>Recommended implementation: The abvm table provides
	positioning information (x,y) to enable mark positioning (GPOS
	lookup type 4, 5).</p><p>Application interface: The application must define the
	GIDs of the base glyphs above which marks need to be
	positioned, and the marks themselves. If these are located in
	the coverage table, the application passes the sequence to the
	abvm table and gets the positioning values (x,y) or
	positioning adjustments for the mark in return.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: Can be used to position default
	marks; or those that have been selected from a number of
	alternates based on contextual requirement using a feature
	like abvs.</p><p>Tag: 'abvs'</p><p>Friendly name: Above-base Substitutions</p><p>Registered by: Microsoft</p><p>Function: Substitutes a ligature for a base glyph and
	mark that's above it.</p><p>Example: In complex scripts like Kannada (Indic), the
	vowel sign for the vowel I which a mark, is positioned above
	base consonants. This mark combines with the consonant Ga to
	form a ligature.</p><p>Recommended implementation: Lookups for this feature map
	each sequence of consonant and vowel sign to the corresponding
	ligature in the font (GSUB lookup type 4).</p><p>Application interface: The application must define the
	GIDs of the base glyphs and the mark that combines with it to
	form a ligature. The application passes the sequence to the
	abvs table. If these are located in the coverage table, it
	gets the GID for the ligature in return.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: None.</p><p>Tag: 'afrc'</p><p>Friendly name: Alternative Fractions</p><p>Registered by: Microsoft</p><p>Function: Replaces figures separated by a slash with an
	alternative form.</p><p>Example: The user enters 3/4 in a recipe and get the
	threequarters nut fraction.</p><p>Recommended implementation: The afrc table maps sets of
	figures separated by slash (U+002F) or fraction (U+2044)
	characters to corresponding fraction glyphs in the font (GSUB
	lookup type 4).</p><p>Application interface: The application must define the
	full sequence of GIDs to be replaced. When the full sequence
	is found in the frac coverage table, the application passes
	the sequence to the afrc table and gets a new GID in return.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'akhn'</p><p>Friendly name: Akhand</p><p>Registered by: Microsoft</p><p>Function: Preferentially substitutes a sequence of
	characters with a ligature. This substitution is done
	irrespective of any characters that may precede or follow the
	sequence.</p><p>Example: In complex scripts like Devanagari (Indic), the
	sequence Ka, Halant, Ssa should always produce the ligature
	Kssa, irrespective of characters that precede/follow the above
	given sequence. The Kssa is identified in Devanagari as an
	Akhand character (meaning unbreakable).</p><p>Recommended implementation: This feature maps the
	sequences for generating Akhands defined in the given script,
	to the ligature they form (GSUB lookup type 4).</p><p>Application interface: The application passes the full
	sequence of GIDs. If these are located in the coverage table
	of the Akhand table, the application gets back the GID for the
	akhand ligature in return.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in most Indic
	scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'blwf'</p><p>Friendly name: Below-base Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the below-base form of a consonant
	in conjuncts.</p><p>Example: In complex scripts like Oriya (Indic), the
	consonant Va has a below-base form that is used to generate
	conjuncts. Given a sequence Gha, Virama (Halant), Va; the
	below-base form of Va would be substituted to form the
	conjunct GhVa.</p><p>Recommended implementation: This feature substitutes the
	GID sequence of consonant followed by (virama) halant; by the
	GID of the below base form of the consonant (GSUB lookup type
	4).</p><p>Application interface: In a conjunct formation sequence,
	if a consonant is identified as having a below base form, the
	application gets back the GID for this. The application may
	also choose to position this glyph if required, after this
	feature is called.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in a number of
	Indic scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'blwm'</p><p>Friendly name: Below-base Mark Positioning</p><p>Registered by: Microsoft</p><p>Function: Positions marks below base glyphs.</p><p>Example: In complex scripts like Gujarati (Indic), the
	vowel sign U needs to be positioned below base
	consonant/conjuncts that form the base glyph. This position
	can vary depending on the base glyph, as well as the
	presence/absence of other marks below the base glyph.</p><p>Recommended implementation: The blwm table provides
	positioning information (x,y) to enable mark positioning (GPOS
	lookup type 4, 5).</p><p>Application interface: The application must define the
	GIDs of the base glyphs below which marks need to be
	positioned, and the marks themselves. If these are located in
	the coverage table, the application passes the sequence to the
	blwm table and gets the positioning values (x,y) or
	positioning adjustments for the mark in return.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: Can be used to position default
	marks; or those that have been selected from a number of
	alternates based on contextual requirement using a feature
	like blws.</p><p>Tag: "blws"</p><p>Friendly name: Below-base Substitutions</p><p>Registered by: Microsoft</p><p>Function: Produces ligatures that comprise of base glyph
	and below-base forms.</p><p>Example: In the Malayalam script (Indic), the conjunct
	Kla, requires a ligature which is formed using the base glyph
	Ka and the below-base form of consonant La. This feature can
	also be used to substitute ligatures formed using base glyphs
	and below base matras in Indic scripts.</p><p>Recommended implementation: The blws table maps the
	identified conjunct forming sequences; or consonant vowel sign
	sequences; to their ligatures (GSUB lookup type 4).</p><p>Application interface: For GIDs found in the blws
	coverage table, the application passes the sequence of GIDs to
	the table, and gets back the GID for the ligature.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'calt'</p><p>Friendly name: Contextual Alternates</p><p>Registered by: Adobe</p><p>Function: In specified situations, replaces default
	glyphs with alternate forms which provide better joining
	behavior. Used in script typefaces which are designed to have
	some or all of their glyphs join.</p><p>Example: In Caflisch Script, o is replaced by o.alt2
	when followed by an ascending letterform.</p><p>Recommended implementation: The calt table specifies the
	context in which each substitution occurs, and maps one or
	more default glyphs to replacement glyphs (GSUB lookup type
	6).</p><p>Application interface: The application passes sequences
	of GIDs to the feature table, and gets back new GIDs. Note
	that full sequences must be passed.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: Not applicable to
	ideographic scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'case'</p><p>Friendly name: Case-Sensitive Forms</p><p>Registered by: Adobe</p><p>Function: Shifts various punctuation marks up to a
	position that works better with all-capital sequences or sets
	of lining figures; also changes oldstyle figures to lining
	figures. By default, glyphs in a text face are designed to
	work with lowercase characters. Some characters should be
	shifted vertically to fit the higher visual center of
	all-capital or lining text. Also, lining figures are the same
	height (or close to it) as capitals, and fit much better with
	all-capital text.</p><p>Example: The user selects a block of text and applies
	this feature. The dashes, bracketing characters, guillemet
	quotes and the like shift up to match the capitals, and
	oldstyle figures change to lining figures.</p><p>Recommended implementation: The font may implement this
	change by substituting different glyphs (GSUB lookup type 1)
	or by repositioning the original glyphs (GPOS lookup type 1).</p><p>Application interface: The application queries whether
	specific GIDs are found in the coverage table for the case
	feature. If so, it passes these IDs to the table and gets back
	either new GIDs or positional adjustments (XPlacement and
	YPlacement).</p><p>UI suggestion: It would be good to apply this feature
	(or turn it off) by default when the user changes case on a
	sequence of more than one character. Applications could also
	detect words consisting only of capitals, and apply this
	feature based on user preference settings.</p><p>Script/language sensitivity: Applies only to European
	scripts; particularly prominent in Spanish-language setting.</p><p>Feature interaction: This feature overrides the results
	of other features affecting the figures (e.g. onum and tnum).</p><p>Tag: "ccmp"</p><p>Friendly name: Glyph Composition/Decomposition</p><p>Registered by: Microsoft</p><p>Function: To minimize the number of glyph alternates, it
	is sometimes desired to decompose a character into two
	glyphs. Additionally, it may be preferable to compose two
	characters into a single glyph for better glyph
	processing. This feature permits such
	composition/decompostion. The feature should be processed as
	the first feature processed, and should be processed only when
	it is called.</p><p>Example: In Syriac, the character 0x0732 is a combining
	mark that has a dot above AND a dot below the base
	character. To avoid multiple glyph variants to fit all base
	glyphs, the character is decomposed into two glyphs...a dot
	above and a dot below. These two glyphs can then be correctly
	placed using GPOS. In Arabic it might be preferred to combine
	the shadda with fatha (0x0651, 0x064E) into a ligature before
	processing shapes. This allows the font vendor to do special
	handling of the mark combination when doing further processing
	without requiring larger contextual rules.</p><p>Recommended implementation: The ccmp table maps the
	character sequence to its corresponding ligature (GSUB lookup
	type 4) or string of glyphs (GSUB lookup type 2). When using
	GSUB lookup type 4, sequences that are made up of larger
	number of glyphs must be placed before those that require
	fewer glyphs.</p><p>Application interface: For GIDs found in the ccmp
	coverage table, the application passes the sequence of GIDs to
	the table, and gets back the GID for the ligature, or GIDs for
	the multiple substitution.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature needs to be
	implemented prior to any other feature.</p><p>Tag: 'clig'</p><p>Friendly name: Contextual Ligatures</p><p>Registered by: Adobe</p><p>Function: Replaces a sequence of glyphs with a single
	glyph which is preferred for typographic purposes. Unlike
	other ligature features, clig specifies the context in which
	the ligature is recommended. This capability is important in
	some script designs and for swash ligatures.</p><p>Example: The glyph for ft replaces the sequence f t in
	Bickham Script, except when preceded by an ascending letter.</p><p>Recommended implementation: The clig table maps
	sequences of glyphs to corresponding ligatures in a chained
	context (GSUB lookup type 8). Ligatures with more components
	must be stored ahead of those with fewer components in order
	to be found. The set of contextual ligatures will vary by
	design and script.</p><p>Application interface: For sets of GIDs found in the
	clig coverage table, the application passes the sequence of
	GIDs to the table and gets back a single new GID. Note that
	full sequences must be passed. Note: This may include a change
	of character code. Besides the original character code, the
	application should store the code for the new character.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: Applies to virtually all
	scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also dlig.</p><p>Tag: 'cpsp'</p><p>Friendly name: Capital Spacing</p><p>Registered by: Adobe</p><p>Function: Globally adjusts inter-glyph spacing for
	all-capital text. Most typefaces contain capitals and
	lowercase characters, and the capitals are positioned to work
	with the lowercase. When capitals are used for words, they
	need more space between them for legibility and
	esthetics. This feature would not apply to monospaced
	designs. Of course the user may want to override this behavior
	in order to do more pronounced letterspacing for esthetic
	reasons.</p><p>Example: The user sets a title in all caps, and the
	Capital Spacing feature opens the spacing.</p><p>Recommended implementation: The cpsp table stores
	alternate advance widths for the capital letters covered,
	generally increasing them by a uniform percentage (GPOS lookup
	type 1).</p><p>Application interface: For GIDs found in the cpsp
	coverage table, the application passes a sequence of GIDs to
	the cpsp table and gets back a set of XPlacement and XAdvance
	adjustments. The application may rely on the user to apply
	this feature (e.g., by selecting text for a change to
	all-caps) or apply its own heuristics for recognizing words
	consisting of capitals.</p><p>UI suggestion: This feature should be on by
	default. Applications may want to allow the user to respecify
	the percentage to fit individual tastes and functions.</p><p>Script/language sensitivity: Should not be used in
	connecting scripts (e.g. most Arabic).</p><p>Feature interaction: May be used in addition to any
	other feature (note specifically that this feature is additive
	with other GPOS features like kern).</p><p>Tag: 'cswh'</p><p>Friendly name: Contextual Swash</p><p>Registered by: Adobe</p><p>Function: This feature replaces default character glyphs
	with corresponding swash glyphs in a specified context. Note
	that there may be more than one swash alternate for a given
	character.</p><p>Example: The user sets the word "HOLIDAY" in Poetica
	with this feature active, and is presented with a choice of
	three alternate forms appropriate for an initial H and one
	alternate appropriate for a medial L.</p><p>Recommended implementation: The cswh table maps GIDs for
	default forms to those for one or more corresponding swash
	forms in a chained context, which may require a selection from
	a set (GSUB lookup type 8). If several styles of swash are
	present across the font, the set of forms for each character
	should be ordered consistently.</p><p>Application interface: For GIDs found in the cswh
	coverage table, the application passes the GIDs to the swsh
	table and gets back one or more new GIDs. If more than one GID
	is returned, the application must provide a means for the user
	to select the one desired.</p><p>UI suggestion: This feature should be inactive by
	default. When more than one GID is returned, an application
	could display the forms sequentially in context, or present a
	palette showing all the forms at once, or give the user a
	choice between these approaches. The application may assume
	that the first glyph in a set is the preferred form, so the
	font developer should order them accordingly.</p><p>Script/language sensitivity: Does not apply to
	ideographic scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also swsh and init.</p><p>Tag: "curs"</p><p>Friendly name: Cursive Positioning</p><p>Registered by: Microsoft</p><p>Function: In cursive scripts like Arabic, this feature
	cursively positions adjacent glyphs.</p><p>Example: In Arabic, the Meem followed by a Reh are
	cursively positioned by overlapping the exit point of the Meem
	on the entry point of the Reh.</p><p>Recommended implementation: The curs table provides
	entry and exit points (x,y) for glyphs to be cursively
	positioned (GPOS lookup type 3).</p><p>Application interface: For GIDs located in the coverage
	table, the application gets back positioning point locations
	for the preceding and following glyphs.</p><p>UI suggestion: This feature could be made active or
	inactive by default, at the user's preference.</p><p>Script/language sensitivity: Can be used in any cursive
	script.</p><p>Feature interaction: None.</p><p>Tag:'c2pc'</p><p>Friendly name: Petite Capitals From Capitals</p><p>Registered by: Tiro Typeworks / Emigre</p><p>Function: This feature turns capital characters into
	petite capitals. It is generally used for words which would
	otherwise be set in all caps, such as acronyms, but which are
	desired in petite-cap form to avoid disrupting the flow of
	text. See the pcap feature description for notes on the
	relationship of caps, smallcaps and petite caps.</p><p>Example: The user types UNICEF or NASA, applies c2pc and
	gets petite cap text.</p><p>Recommended implementation: The c2pc table maps capital
	glyphs to the corresponding petite cap forms (GSUB lookup type
	1).</p><p>Application interface: For GIDs found in the c2pc
	coverage table, the application passes GIDs to the c2pc table,
	and gets back new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to scripts
	with both upper- and lowercase forms (e.g. Latin, Cyrillic,
	Greek).</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. Also see pcap.</p><p>Tag: 'c2sc'</p><p>Friendly name: Small Capitals From Capitals</p><p>Registered by: Adobe</p><p>Function: This feature turns capital characters into
	small capitals. It is generally used for words which would
	otherwise be set in all caps, such as acronyms, but which are
	desired in small-cap form to avoid disrupting the flow of
	text.</p><p>Example: The user types UNICEF or SCUBA, applies c2sc
	and gets small cap text.</p><p>Recommended implementation: The c2sc table maps capital
	glyphs to the corresponding small-cap forms (GSUB lookup type
	1).</p><p>Application interface: For GIDs found in the c2sc
	coverage table, the application passes GIDs to the c2sc table,
	and gets back new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to European
	scripts (Cyrillic, Greek and Latin), which have capital forms.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. Also see smcp.</p><p>Tag: "dist"</p><p>Friendly name: Distances</p><p>Registered by: Microsoft</p><p>Function: Provides a means to control distance between
	glyphs.</p><p>Example: In the Devanagari (Indic) script, the distance
	between the vowel sign U and a consonant can be adjusted using
	this.</p><p>Recommended implementation: The dist table provides
	distances by which a glyph needs to move towards or away from
	another glyph (GPOS lookup type 2).</p><p>Application interface: For GIDs found in the dist
	coverage table, the application passes their GID to the table
	and gets back the distance that needs to be maintained between
	them.</p><p>UI suggestion: This feature could be made active or
	inactive by default, at the user's preference.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: None.</p><p>Tag: 'dlig'</p><p>Friendly name: Discretionary Ligatures</p><p>Registered by: Adobe</p><p>Function: Replaces a sequence of glyphs with a single
	glyph which is preferred for typographic purposes. This
	feature covers those ligatures which may be used for special
	effect, at the user's preference.</p><p>Example: The glyph for ct replaces the sequence of
	glyphs c t, or U+322E (Kanji ligature for "Friday") replaces
	the sequence U+91D1 U+66DC U+65E5.</p><p>Recommended implementation: The dlig table maps
	sequences of glyphs to corresponding ligatures (GSUB lookup
	type 4). Ligatures with more components must be stored ahead
	of those with fewer components in order to be found. The set
	of discretionary ligatures will vary by design and script.</p><p>Application interface: For sets of GIDs found in the
	dlig coverage table, the application passes the sequence of
	GIDs to the table and gets back a single new GID. Note that
	full sequences must be passed. This may include a change of
	character code. Besides the original character code, the
	application should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies to virtually all
	scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also clig.</p><p>Tag: 'dnom'</p><p>Friendly name: Denominators</p><p>Registered by: Adobe</p><p>Function: Replaces selected figures which follow a slash
	with denominator figures.</p><p>Example: In the string 11/17 selected by the user, the
	application turns the 17 into denominators when the user
	applies the fraction feature (frac).</p><p>Recommended implementation: The dnom table maps sets of
	figures and related characters to corresponding numerator
	glyphs in the font (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the dnom
	coverage table, the application passes a GID to the table and
	gets back a new GID.</p><p>UI suggestion: This feature should normally be called by
	an application when the user applies the frac feature.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature supports frac. It may
	be used in combination with other substitution (GSUB)
	features, whose results it may override.</p><p>Tag: 'expt'</p><p>Friendly name: Expert Forms</p><p>Registered by: Adobe</p><p>Function: Like the JIS78 Forms described above, this
	feature replaces standard forms in Japanese fonts with
	corresponding forms preferred by typographers. Although most
	of the JIS78 substitutions are included, the expert
	substitution goes on to handle many more characters.</p><p>Example: The user would invoke this feature to replace
	kanji character U+5516 with U+555E.</p><p>Recommended implementation: The expt table maps many
	default (JIS90) GIDs to corresponding alternates (GSUB lookup
	type 1).</p><p>Application interface: For GIDs found in the expt
	coverage table, the application passes the GIDs to the table
	and gets back one new GID for each. Note: This is a change of
	character code. Besides the original character code, the
	application should store the code for the new character.</p><p>UI suggestion: Applications may choose to have this
	feature active or inactive by default, depending on their
	target markets.</p><p>Script/language sensitivity: Applies only to Japanese.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when it's
	applied, except the palt, vpal, vert and vrt2 features, which
	may be used in addition.</p><p>Tag:  "falt"</p><p>Friendly name: Final Glyph on Line Alternates</p><p>Registered by: Microsoft</p><p>Function: Replaces line final glyphs with alternate
	forms specifically designed for this purpose (they would have
	less or more advance width as need may be), to help
	justification of text.</p><p>Example: In the Arabic script, providing alternate forms
	for line final glyphs would result in better
	justification. eg. replacing a long tailed Yeh-with-tail with
	one that has a slightly longer/shorter tail.</p><p>Recommended implementation: The falt table maps line
	final glyphs (in isolated or final forms) to their
	corresponding alternate forms (GSUB lookup type 3).</p><p>Application interface: For GIDs found in the falt
	coverage table, the application passes a GID to the table and
	gets back a new GID.</p><p>UI suggestion: This feature could be made active or
	inactive by default, at the user's preference.</p><p>Script/language sensitivity: Can be used in any cursive
	script.</p><p>Feature interaction: Would need to be applied last, only
	after all other features have been applied to the run.</p><p>Tag: "fin2"</p><p>Friendly name: Terminal Form #2</p><p>Registered by: Microsoft</p><p>Function: Replaces the Alaph glyph at the end of Syriac
	words with its appropriate form, when the preceding base
	character cannot be joined to, and that preceding base
	character is not a Dalath, Rish, or dotless Dalath-Rish.</p><p>Example: When an Alaph is preceded by a He, the Alaph
	  would be replaced by an appropriate form. This feature is
	  used only for the Syriac script alaph character.</p><p>Recommended implementation: The fin2 table maps default
	alphabetic forms to corresponding final forms (GSUB lookup
	type 5).</p><p>Application interface: The application is responsible
	for noting word boundaries. For GIDs in the middle of words
	and found in the fin2 coverage table, the application passes a
	GID to the feature and gets back a new GID.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Used only with the Syriac
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also init and fina.</p><p>Tag: "fin3"</p><p>Friendly name: Terminal Form #3</p><p>Registered by: Microsoft</p><p>Function: Replaces Alaph glyphs at the end of Syriac
	words when the preceding base character is a Dalath, Rish, or
	dotless Dalath-Rish.</p><p>Example: When an Alaph is preceded by a Dalath, the
	  Alaph would be replaced by an appropriate form.
	  This feature is used only for the Syriac script alaph character.</p><p>Recommended implementation: The fin3 table maps default
	alphabetic forms to corresponding final forms (GSUB lookup
	type 5).</p><p>Application interface: The application is responsible
	for noting word boundaries. For GIDs in the middle of words
	and found in the fin3 coverage table, the application passes a
	GID to the feature and gets back a new GID.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Used only with the Syriac
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also init and fina.</p><p>Tag: 'fina'</p><p>Friendly name: Terminal Forms</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces glyphs at the ends of words with
	alternate forms designed for this use. This is common in Latin
	connecting scripts, and required in various non-Latins like
	Arabic.</p><p>Example: In the typeface Poetica, the default e in the
	word 'type' is replaced with the e.end form.</p><p>Recommended implementation: The fina table maps default
	alphabetic forms to corresponding ending forms (GSUB lookup
	type 1).</p><p>Application interface: The application is responsible
	for noting word boundaries. For GIDs at the ends of words and
	found in the fina coverage table, the application passes a GID
	to the feature and gets back a new GID.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: Can be used in any
	alphabetic script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also init and medi.</p><p>Tag: 'frac'</p><p>Friendly name: Fractions</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces figures separated by a slash with
	'common' (diagonal) fractions.</p><p>Example: The user enters 3/4 in a recipe and gets the
	threequarters fraction.</p><p>Recommended implementation: The frac table maps sets of
	figures separated by slash or fraction characters to
	corresponding fraction glyphs in the font. These may be
	precomposed fractions (GSUB lookup type 4) or arbitrary
	fractions (GSUB lookup type 1).</p><p>Application interface: The application must define the
	full sequence of GIDs to be replaced, based on user input
	(i.e. user selection determines the string's
	delimitation). When the full sequence is found in the frac
	coverage table, the application passes the sequence to the
	frac table and gets a new GID in return. When the frac table
	does not contain an exact match, the application performs two
	steps. First, it uses the numr feature (see below) to replace
	figures (as used in the numr coverage table) preceding the
	slash with numerators, and to replace the typographic slash
	character (U+002F) with the fraction slash character
	(U+2044). Second, it uses the dnom feature (see below) to
	replace all remaining figures (as listed in the dnom coverage
	table) with denominators.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may require the
	application to call the numr and dnom features. It may be used
	in combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'fwid'</p><p>Friendly name: Full Widths</p><p>Registered by: Adobe</p><p>Function: Replaces glyphs set on other widths with
	glyphs set on full (usually em) widths. In a CJKV font, this
	may include "lower ASCII" Latin characters and various
	symbols. In a European font, this feature replaces
	proportionally-spaced glyphs with monospaced glyphs, which are
	generally set on widths of 0.6 em.</p><p>Example: The user may invoke this feature in a Japanese
	font to get full monospaced Latin glyphs instead of the
	corresponding proportionally-spaced versions.</p><p>Recommended implementation: The font may contain
	alternate glyphs designed to be set on full widths (GSUB
	lookup type 1), or it may specify alternate (full-width)
	metrics for the proportional glyphs (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the fwid
	coverage table, the application passes the GIDs to the table
	and gets back either new GIDs or positional adjustments
	(XPlacement and XAdvance).</p><p>UI suggestion: This feature would normally be off by
	default.</p><p>Script/language sensitivity: Applies to any script which
	can use monospaced forms.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. tnum, halt, hwid,
	palt, pwid, qwid and twid), which should be turned off when
	it's applied. It deactivates the kern feature.</p><p>Tag: "half"</p><p>Friendly name: Half Forms</p><p>Registered by: Microsoft</p><p>Function: Produces the half forms of consonants in Indic
	scripts.</p><p>Example: In Hindi (Devanagari script), the conjunct KKa,
	obtained by doubling the Ka, is denoted with a half form of Ka
	followed by the full form.</p><p>Recommended implementation: The half table maps the
	sequence of a consonant followed by a virama (halant) to its
	half form (GSUB lookup type 4).</p><p>Application interface: For substitution sequences
	defined in the half table [consonant followed by the virama
	(halant)], the application passes the sequence of GIDs to the
	table, and gets back the GID for the half form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts
	that show similarity to Devanagari.</p><p>Feature interaction: This feature overrides the results
	of all other features, except akhn .</p><p>Tag: "haln"</p><p>Friendly name: Halant Forms</p><p>Registered by: Microsoft</p><p>Function: Produces the halant forms of consonants in
	Indic scripts.</p><p>Example: In Sanskrit (Devanagari script), syllable final
	consonants are frequently required in their halant form.</p><p>Recommended implementation: The haln table maps the
	sequence of a consonant followed by a virama (halant) to its
	halant form (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	halant table, the application passes the sequence of GIDs to
	the feature (essentially the consonant and virama), and gets
	back the GID for the halant form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'halt'</p><p>Friendly name: Alternate Half Widths</p><p>Registered by: Adobe</p><p>Function: Respaces glyphs designed to be set on full-em
	widths, fitting them onto half-em widths. This differs from
	hwid in that it does not substitute new glyphs.</p><p>Example: The user may invoke this feature in a CJKV font
	to get better fit for punctuation or symbol glyphs without
	disrupting the monospaced alignment.</p><p>Recommended implementation: The font specifies alternate
	metrics for the full-width glyphs (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the halt
	coverage table, the application passes the GIDs to the table
	and gets back positional adjustments (XPlacement, XAdvance,
	YPlacement and YAdvance).</p><p>UI suggestion: This feature would be off by default.</p><p>Script/language sensitivity: Used only in CJKV fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. tnum, fwid, hwid,
	palt, twid), which should be turned off when it's applied. It
	deactivates the kern feature. See also vhal.</p><p>Tag: 'hist'</p><p>Friendly name: Historical Forms</p><p>Registered by: Microsoft/Adobe</p><p>Function: Some letterforms were in common use in the
	past, but appear anachronistic today. The best-known example
	is the long form of s; others would include the old Fraktur
	k. Some fonts include the historical forms as alternates, so
	they can be used for a 'period' effect. This feature replaces
	the default (current) forms with the historical
	alternates. While some ligatures are also used for historical
	effect, this feature deals only with single characters.</p><p>Example: The user applies this feature in Adobe Jenson
	to get the archaic forms of M, Q and Z.</p><p>Recommended implementation: The hist table maps default
	forms to corresponding historical forms (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the hist
	coverage table, the application passes the GIDs to the hist
	table and gets back new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'hkna'</p><p>Friendly name: Horizontal Kana Alternates</p><p>Registered by: Adobe</p><p>Function: Replaces standard kana with forms that have
	been specially designed for only horizontal writing. This is a
	typographic optimization for improved fit and more even
	color. Also see vkna.</p><p>Example: Standard full-width kana (hiragana and
	katakana) are replaced by forms that are designed for
	horizontal use.</p><p>Recommended implementation: The font includes a set of
	specially-designed glyphs, listed in the hkna coverage
	table. The hkna feature maps the standard full-width forms to
	the corresponding special horizontal forms (GSUB lookup type
	1).</p><p>Application interface: For GIDs found in the hkna
	coverage table, the application passes GIDs to the feature,
	and gets back new GIDs.</p><p>UI suggestion:This feature would be off by default.</p><p>Script/language sensitivity: Applies only to fonts that
	support kana (hiragana and katakana).</p><p>Feature interaction: This feature may be used with the
	kern feature. Since it is for horizontal use, features
	applying to vertical behaviors (e.g. vkna, vert, vrt2 or vkrn)
	do not apply.</p><p>Tag: 'hlig'</p><p>Friendly name: Historical Ligatures</p><p>Registered by: Microsoft</p><p>Function: Some ligatures were in common use in the past,
	but appear anachronistic today. Some fonts include the
	historical forms as alternates, so they can be used for a
	'period' effect. This feature replaces the default (current)
	forms with the historical alternates.</p><p>Example: The user applies this feature using Palatino
	Linotype, and historic ligatures are formed for all long s
	forms, including: long s+t, long s+b, long s+h, long s+k, and
	several others.</p><p>Recommended implementation: The hlig table maps default
	ligatures and character combinations to corresponding
	historical ligatures (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the hlig
	coverage table, the application passes the GIDs to the hlig
	table and gets back new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'hngl'</p><p>Friendly name: Hangul</p><p>Registered by: Adobe</p><p>Function: Replaces hanja (Chinese-style) Korean
	characters with the corresponding hangul (syllabic)
	characters. This effectively reverses the standard input
	method, in which hangul are entered and replaced by
	hanja. Many of these substitutions are one-to-one (GSUB lookup
	type 1), but hanja substitution often requires the user to
	choose from several possible hangul characters (GSUB lookup
	type 3).</p><p>Example: The user may call this feature to get U+AC00
	from U+4F3D.</p><p>Recommended implementation: This table associates each
	hanja character in the font with one or more hangul
	characters. The manufacturer may choose to build two tables
	(one for each lookup type) or only one which uses lookup type
	3 for all substitutions. As in any one-from-many substitution,
	alternates should be ordered consistently across a family, so
	that those alternates can work correctly when switching
	between family members.</p><p>Application interface: For GIDs found in the hngl
	coverage table, the application passes the GIDs to the table
	and gets back one or more new GIDs. If more than one GID is
	returned, the application must provide a means for the user to
	select the one desired. Note: This is a change of semantic
	value. Besides the original character codes (when entered as
	hanja), the application should store the code for the new
	character.</p><p>UI suggestion: This feature should be inactive by
	default. The application may note the user's choice when
	selecting from multiple hangul, and offer it as a default the
	next time the source hanja character is encountered. In the
	absence of such prior information, the application may assume
	that the first hangul in a set is the preferred form, so the
	font developer should order them accordingly.</p><p>Script/language sensitivity: Korean only.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when it's
	applied, except the palt, vert and vrt2 may be used in
	addition.</p><p>Tag: 'hwid'</p><p>Friendly name: Half Widths</p><p>Registered by: Adobe</p><p>Function: Replaces glyphs on proportional widths, or
	fixed widths other than half an em, with glyphs on half-em
	(en) widths. Many CJKV fonts have glyphs which are set on
	multiple widths; this feature selects the half-em
	version. There are various contexts in which this is the
	preferred behavior, including compatibility with older desktop
	documents.</p><p>Example: The user may replace a proportional Latin glyph
	with the same character set on a half-em width.</p><p>Recommended implementation: The font may contain
	alternate glyphs designed to be set on half-em widths (GSUB
	lookup type 1), or it may specify alternate metrics for the
	original glyphs (GPOS lookup type 1) which adjust their
	spacing to fit in half-em widths.</p><p>Application interface: For GIDs found in the hwid
	coverage table, the application passes the GIDs to the table
	and gets back either new GIDs or positional adjustments
	(XPlacement and XAdvance).</p><p>UI suggestion: This feature would normally be off by
	default.</p><p>Script/language sensitivity: Generally used only in CJKV
	fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. tnum, fwid, halt,
	qwid and twid), which should be turned off when it's
	applied. It deactivates the kern feature.</p><p>Tag: 'init'</p><p>Friendly name: Initial Forms</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces glyphs at the beginnings of words
	with alternate forms designed for this use. This is common in
	Latin connecting scripts, and required in various non-Latins
	like Arabic.</p><p>Example: In the typeface Ex Ponto, the default t in the
	word 'type' is replaced with the t.begin form.</p><p>Recommended implementation: The init table maps default
	alphabetic forms to corresponding beginning forms (GSUB lookup
	type 1).</p><p>Application interface: The application is responsible
	for noting word boundaries. For GIDs at the beginnings of
	words and found in the init coverage table, the application
	passes a GID to the feature and gets back a new GID.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: Can be used in any
	alphabetic script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also medi and fina.</p><p>Tag: "isol"</p><p>Friendly name: Isolated Forms</p><p>Registered by: Microsoft</p><p>Function: Replaces the nominal form of glyphs with their
	isolated forms.</p><p>Example: In Arabic, if the Alef is followed by Lam, the
	default glyph for Alef is replaced with its isolated form.</p><p>Recommended implementation: The isol table maps default
	alphabetic forms to corresponding isolated forms (GSUB lookup
	type 1).</p><p>Application interface: For GIDs found in the isol
	coverage table, the application passes a GID to the feature
	and gets back a new GID for the isolated form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Can be used in any cursive
	script.</p><p>Feature interaction: This feature overrides the results
	of all other features. See also init, medi, fina.</p><p>Tag: 'ital'</p><p>Friendly name: Italics</p><p>Registered by: Adobe</p><p>Function: Some fonts (such as Adobe's Pro Japanese
	fonts) will have both Roman and Italic forms of some
	characters in a single font. This feature replaces the Roman
	glyphs with the corresponding Italic glyphs.</p><p>Example: The user would apply this feature to replace B
	with B.</p><p>Recommended implementation: The ital table maps the
	Roman forms in a font to the corresponding Italic forms (GSUB
	lookup type 1).</p><p>Application interface: For GIDs found in the ital
	coverage table, the application passes the GIDs to the table
	and gets back one new GID for each.</p><p>UI suggestion: When a user selects text and applies an
	Italic style, an application should check for this feature and
	use it if present.</p><p>Script/language sensitivity: Applies mostly to Latin;
	note that many non-Latin fonts contain Latin as well.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. In CJKV fonts it should activate the
	kern feature (which would be on anyway in other scripts).</p><p>Tag: "jalt"</p><p>Friendly name: Justification Alternates</p><p>Registered by: Microsoft</p><p>Function: Improves justification of text by replacing
	glyphs with alternate forms specifically designed for this
	purpose (they would have less or more advance width as need
	may be).</p><p>Example: In the Arabic script, providing alternate forms
	for line final glyphs would result in better justification and
	reduce the use of tatweels (Kashidas). eg. replacing a Swash
	Kaf with an alternate form.</p><p>Recommended implementation: The jalt table maps the
	initial, medial, final or isolated forms to their
	corresponding alternate forms (GSUB lookup type 3).</p><p>Application interface: The application is responsible
	for noting line ends/boundaries. For GIDs found in the jalt
	coverage table, the application passes a GID to the feature
	and gets back a new GID.</p><p>UI suggestion: This feature could be made active or
	inactive by default, at the user's preference.</p><p>Script/language sensitivity: Can be used in any cursive
	script.</p><p>Feature interaction: If the font contains init, medi,
	fina, isol features, these need to be called prior to calling
	this feature.</p><p>Tag: 'jp78'</p><p>Friendly name: JIS78 Forms</p><p>Registered by: Adobe</p><p>Function: This feature replaces default (JIS90) Japanese
	glyphs with the corresponding forms from the JIS C 6226-1978
	(JIS78) specification.</p><p>Example: The user would invoke this feature to replace
	kanji character U+5516 with U+555E.</p><p>Recommended implementation: When JIS90 glyphs correspond
	to JIS78 forms, the jp78 table maps each of those glyphs to
	their alternates. While many of these substitutions are
	one-to-one (GSUB lookup type 1), others require a selection
	from a set (GSUB lookup type 3). The manufacturer may choose
	to build two tables (one for each lookup type) or only one
	which uses lookup type 3 for all substitutions.</p><p>Application interface: For GIDs found in the jp78
	coverage table, the application passes the GIDs to the table
	and gets back one or more new GIDs. If more than one GID is
	returned, the application must provide a means for the user to
	select the one desired. The application may assume that the
	first glyph in a set is the preferred form, so the font
	developer should order them accordingly. Note: This is a
	change of character code. Besides the original character code,
	the application should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to Japanese.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when it's
	applied, except the palt, vpal, vert and vrt2 features, which
	may be used in addition.</p><p>Tag: 'jp83'</p><p>Friendly name: JIS83 Forms</p><p>Registered by: Adobe</p><p>Function: This feature replaces default (JIS90) Japanese
	glyphs with the corresponding forms from the JIS X 0208-1983
	(JIS83) specification.</p><p>Example: Because of the Han unification in Unicode,
	there are no JIS83 glyphs which have distinct Unicode values,
	so the substitution cannot be described specifically.</p><p>Recommended implementation: When JIS90 glyphs correspond
	to JIS83 forms, the jp83 table maps each of those glyphs to
	their alternates (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the jp83
	coverage table, the application passes the GIDs to the table
	and gets back one or more new GIDs. If more than one GID is
	returned, the application must provide a means for the user to
	select the one desired.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to Japanese.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when it's
	applied, except the palt, vpal, vert and vrt2 features, which
	may be used in addition.</p><p>Tag: 'jp90'</p><p>Friendly name: JIS90 Forms</p><p>Registered by: Adobe</p><p>Function: This feature replaces Japanese glyphs from the
	JIS78 or JIS83 specifications with the corresponding forms
	from the JIS X 0208-1990 (JIS90) specification.</p><p>Example: The user would invoke this feature to replace
	kanji character U+555E with U+5516.</p><p>Recommended implementation: The jp90 table maps each
	JIS78 and JIS83 form in a font to JIS90 forms (GSUB lookup
	type 1). The application stores a record of any simplified
	forms which resulted from substitutions (the jp78 or jp83
	features); for such forms, applying the jp90 feature undoes
	the previous substitution. When there is no record of a
	substitution, the application uses the jp90 table to get back
	to the default form.</p><p>Application interface: For GIDs found in the jp90
	coverage table, the application passes the GIDs to the table
	and gets back one new GID for each. Note: This is a change of
	character code. Besides the original character code, the
	application should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to Japanese.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when it's
	applied, except the palt, vpal, vert and vrt2 features, which
	may be used in addition.</p><p>Tag: 'kern'</p><p>Friendly name: Kerning</p><p>Registered by: Microsoft/Adobe</p><p>Function: Adjusts amount of space between glyphs,
	generally to provide optically consistent spacing between
	glyphs. Although a well-designed typeface has consistent
	inter-glyph spacing overall, some glyph combinations require
	adjustment for improved legibility. Besides standard
	adjustment in the horizontal direction, this feature can
	supply size-dependent kerning data via device tables,
	"cross-stream" kerning in the Y text direction, and adjustment
	of glyph placement independent of the advance adjustment. Note
	that this feature may apply to runs of more than two glyphs,
	and would not be used in monospaced fonts. Also note that this
	feature does not apply to text set vertically.</p><p>Example: The o is shifted closer to the T in the
	combination "To."</p><p>Recommended implementation: The font stores a set of
	adjustments for pairs of glyphs (GPOS lookup type 2 or
	8). These may be stored as one or more tables matching left
	and right classes, and/or as individual pairs. Additional
	adjustments may be provided for larger sets of glyphs
	(e.g. triplets, quadruplets, etc.) to overwrite the results of
	pair kerns in particular combinations.</p><p>Application interface: The application passes a sequence
	of GIDs to the kern table, and gets back adjusted positions
	(XPlacement, XAdvance, YPlacement and YAdvance) for those
	GIDs. When using the type 2 lookup on a run of glyphs, it's
	critical to remember to not consume the last glyph, but to
	keep it available as the first glyph in a subsequent run (this
	is a departure from normal lookup behavior).</p><p>UI suggestion: This feature should be active by default
	for horizontal text setting. Applications may wish to allow
	users to add further manually-specified adjustments to suit
	specific needs and tastes.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: If 'kern' is activated, 'palt' must
	also be activated if it exists. (If 'palt' is activated, there
	is no requirement that 'kern' must also be activated.) May be
	used in addition to any other feature except those which
	result in fixed (uniform) advance widths (e.g. fwid, halt,
	hwid, qwid and twid).</p><p>Tag: 'lfbd'</p><p>Friendly name: Left Bounds</p><p>Registered by: Adobe</p><p>Function: Aligns glyphs by their apparent left extents
	at the left ends of horizontal lines of text, replacing the
	default behavior of aligning glyphs by their origins. This
	feature is called by the Optical Bounds ( opbd) feature
	above.</p><p>Example: Succeeding lines beginning with T, D and W
	would shift to the left by varying amounts when the text is
	left-justified and this feature is applied.</p><p>Recommended implementation: Values for affected glyphs
	describe the amount by which the placement and advance width
	should be altered (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the lfbd
	coverage table, the application passes a GID to the table and
	gets back a new XPlacement and XAdvance value.</p><p>UI suggestion: This feature is called by an application
	when the user invokes the opbd feature.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: Should not be applied to glyphs
	which use fixed-width features (e.g. fwid, halt, hwid, qwid
	and twid) or vertical features (e.g. vert, vrt2, vpal, valt
	and vhal). Is called by the opbd feature.</p><p>Tag: 'liga'</p><p>Friendly name: Standard Ligatures</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces a sequence of glyphs with a single
	glyph which is preferred for typographic purposes. This
	feature covers the ligatures which the designer/manufacturer
	judges should be used in normal conditions.</p><p>Example: The glyph for ffl replaces the sequence of
	glyphs f f l.</p><p>Recommended implementation: The liga table maps
	sequences of glyphs to corresponding ligatures (GSUB lookup
	type 4). Ligatures with more components must be stored ahead
	of those with fewer components in order to be found. The set
	of standard ligatures will vary by design and script.</p><p>Application interface: For sets of GIDs found in the
	liga coverage table, the application passes the sequence of
	GIDs to the table and gets back a single new GID. Note that
	full sequences must be passed.</p><p>UI suggestion: This feature serves a critical function
	in some contexts, and should be active by default.</p><p>Script/language sensitivity: Applies to virtually all
	scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: "ljmo"</p><p>Friendly name: Leading Jamo Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the leading jamo form of a
	cluster.</p><p>Example: In Hangul script, the jamo cluster is composed
	of three parts (leading consonant, vowel, and trailing
	consonant). When a sequence of leading class jamos are found,
	their combined leading jamo form is substituted.</p><p>Recommended implementation: The ljmo table maps the
	sequence required to convert a series of jamos into its
	leading jamo form (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	ljmo table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the leading jamo form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required for Hangul script
	when Ancient Hangul writing system is supported.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'lnum'</p><p>Friendly name: Lining Figures</p><p>Registered by: Adobe (Modified by Adobe, this is the
	newer description)</p><p>Function: This feature changes selected figures from
	oldstyle to the default lining form.</p><p>Example: The user invokes this feature in order to get
	lining figures, which fit better with all-capital
	text. Various characters designed to be used with figures may
	also be covered by this feature. In cases where lining figures
	are the default form, this feature would undo previous
	substitutions.</p><p>Recommended implementation: The lnum table maps each
	oldstyle figure, and any associated characters to the
	corresponding lining form (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the lnum
	coverage table, the application passes a GID to the onum table
	and gets back a new GID. Even if the current figures resulted
	from an earlier substitution, it may not be correct to simply
	revert to the original GIDs, because of interaction with the
	figure width features, so it's best to use this table.</p><p>UI suggestion: This feature should be inactive by
	default. Users can switch between the lining and oldstyle sets
	by turning this feature on or off. Note that this feature is
	distinct from the figure width features (pnum and tnum). When
	the user invokes this feature, the application may wish to
	inquire whether a change in width is also desired.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature overrides the results
	of the Oldstyle Figures feature ( onum).</p><p>Tag: 'locl'</p><p>Friendly name: Localized Forms</p><p>Registered by: Tiro Typeworks/Adobe</p><p>Function: Many scripts used to write multiple languages
	over wide geographical areas have developed localized variant
	forms of specific letters, which are used by individual
	literary communities. For example, a number of letters in the
	Bulgarian and Serbian alphabets have forms distinct from their
	Russian counterparts and from each other. In some cases the
	localized form differs only subtly from the script 'norm', in
	others the forms are radically distinct. This feature enables
	localized forms of glyphs to be substituted for default
	forms.</p><p>Example: The user applies this feature to text to enable
	localized Bulgarian forms of Cyrillic letters; alternatively,
	the feature might enable localized Russian forms in a
	Bulgarian manufactured font in which the Bulgarian forms are
	the efault characters.</p><p>Recommended implementation: For a given Unicode value,
	the font contains glyphs for two or more locales. The locl
	table maps GIDs for default forms to GIDs for corresponding
	localized alternatives. These are one-to-one substitutions
	(GSUB lookup type 1).</p><p>Application interface: Localized forms are associated
	with specific languages and are activated by language
	tags. Which glyph is used as the localized form should be
	determined by the language the user has specified. The user
	can switch localized forms by selecting a new language, or may
	enable default forms by switching off the locl feature.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: Applies to all scripts and
	languages; but of course behavior differs by script and
	language.</p><p>Feature interaction: This feature can be used in
	combination with any other feature. It replaces and extends
	the earlier locale-specific tags zhcn, zhtw, jajp, kokr and
	vivn which had been defined for CJKV scripts.</p><p>Tag: 'mark'</p><p>Friendly name: Mark Positioning</p><p>Registered by: Microsoft</p><p>Function: Positions mark glyphs with respect to base
	  glyphs.</p><p>Example: In the Arabic script, positioning the Hamza
	above the Yeh.</p><p>Recommended implementation: This feature may be
	implemented as a MarkToBase Attachment lookup (GPOS LookupType
	= 4) or a MarkToLigature Attachment lookup (GPOS LookupType =
	5).</p><p>Application interface: For GIDs found in the mark
	coverage table, the application gets back the positioning or
	position adjustment values for the mark glyph.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: None.</p><p>Tag: "med2"</p><p>Friendly name: Medial Form #3</p><p>Registered by: Microsoft</p><p>Function: Replaces Alaph glyphs in the middle of Syriac
	words when the preceding base character cannot be joined to.</p><p>Example: When an Alaph is preceded by a Waw, the Alaph
	  would be replaced by an appropriate form.</p><p>This feature is used only for the Syriac script alaph
	character.</p><p>Recommended implementation: The med2 table maps default
	alphabetic forms to corresponding medial forms (GSUB lookup
	type 5).</p><p>Application interface: The application is responsible
	for noting word boundaries. For GIDs in the middle of words
	and found in the med2 coverage table, the application passes a
	GID to the feature and gets back a new GID.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Used only with the Syriac
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also init and fina.</p><p>Tag: 'medi'</p><p>Friendly name: Medial Forms</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces glyphs in the middles of words
	(i.e. following a beginning and preceding an end) with
	alternate forms designed for this use. Note: This is different
	from the default form, which is designed for stand-alone
	use. This is common in Latin connecting scripts, and required
	in various non-Latins like Arabic.</p><p>Example: In the typeface Caflisch Script, the y and p in
	the word 'type' are replaced by the y.med and p.med forms.</p><p>Recommended implementation: The medi table maps default
	alphabetic forms to corresponding medial forms (GSUB lookup
	type 1).</p><p>Application interface: The application is responsible
	for noting word boundaries. For GIDs in the middles of words
	and found in the medi coverage table, the application passes a
	GID to the feature and gets back a new GID.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: Can be used in any
	alphabetic script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also init and fina.</p><p>Tag: 'mgrk'</p><p>Friendly name: Mathematical Greek</p><p>Registered by: Adobe</p><p>Function: Replaces standard typographic forms of Greek
	glyphs with corresponding forms commonly used in mathematical
	notation (which are a subset of the Greek alphabet).</p><p>Example: The user applies this feature to U+03A3
	(Sigma), and gets U+2211 (summation).</p><p>Recommended implementation: The mgrk table maps Greek
	glyphs to the corresponding forms used for mathematics (GSUB
	lookup type 1).</p><p>Application interface: For GIDs found in the mgrk
	coverage table, the application passes a GID to the feature
	table and gets back a new GID. Note: This is a change of
	semantic value. Besides the original character codes, the
	application should store the code for the new character.</p><p>UI suggestion: This feature should be off by default in
	most applications. Math-oriented applications may want to
	activate this feature by default.</p><p>Script/language sensitivity: Could apply to any font
	which includes coverage for the Greek script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: "mkmk"</p><p>Friendly name: Mark to Mark Positioning</p><p>Registered by: Microsoft</p><p>Function: Positions marks with respect to other
	marks. Required in various non-Latin scripts like Arabic.</p><p>Example: In Arabic, the ligaturised mark Ha with Hamza
	above it; can also be obtained by positioning these marks
	relative to one another.</p><p>Recommended implementation: This feature may be
	implemented as a MarkToMark Attachment lookup (GPOS lookup
	type 6).</p><p>Application interface: The application gets back
	positioning values or positional adjustments for marks.</p><p>UI suggestion: This feature should be active by
	default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: None.</p><p>Tag: 'mset'</p><p>Registered by: Microsoft</p><p>Function: Positions Arabic combining marks in fonts for
	  Windows 95 using glyph substitution</p><p>Example: In Arabic, the Hamza is positioned differently
	when placed above a Yeh Barree as compared to the Alef.</p><p>Windows 95 implementation: In contrast to the "mark"
	feature, "mset" uses glyph substitution to combine marks and
	base glyphs. It replaces a default mark glyph with a correctly
	positioned mark glyph. The font designer specifies the
	position of the mark when describing the mark's contour in the
	font file. Microsoft's Arabic fonts, created for Windows 95,
	use a contextual substitution lookup (GSUB LookupType = 5) to
	implement the "mset" feature.</p><p>Tag: 'nalt'</p><p>Friendly name: Alternate Annotation Forms</p><p>Registered by: Adobe</p><p>Function: Replaces default glyphs with various
	notational forms (e.g. glyphs placed in open or solid circles,
	squares, parentheses, diamonds or rounded boxes). In some
	cases an annotation form may already be present, but the user
	may want a different one.</p><p>Example: The user invokes this feature to get U+3200
	(the circled form of 'ga') from U+3131 (hangul 'ga').</p><p>Recommended implementation: The nalt table maps GIDs for
	various standard forms to one or more corresponding annotation
	forms. While many of these substitutions are one-to-one (GSUB
	lookup type 1), others require a selection from a set (GSUB
	lookup type 3). The manufacturer may choose to build two
	tables (one for each lookup type) or only one which uses
	lookup type 3 for all substitutions. If more than one form is
	present, the set of forms for each character should be ordered
	consistently - both within the font and across the family.</p><p>Application interface: For GIDs found in the nalt
	coverage table, the application passes a GID and gets back a
	set of new GIDs, then stores the one selected by the user.</p><p>UI suggestion: This feature should be inactive by
	default. The application must provide a means for the user to
	select the desired form from the set returned by the table. It
	can note the position of the selected form in a set of
	alternates, and offer the glyph at that position as the
	default selection the next time this feature is invoked. In
	the absence of such prior information, the application may
	assume that the first glyph in a set is the preferred form, so
	the font developer should order them accordingly.</p><p>Script/language sensitivity: Used mostly in CJKV fonts,
	but can apply to European scripts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when it's
	applied, except the vert and vrt2 features, which may be used
	in addition.</p><p>Tag: "nlck"</p><p>Friendly name: NLC Kanji Forms</p><p>Registered by: Adobe Systems Inc.</p><p>Function: The National Language Council (NLC) of Japan
	has defined new glyph shapes for a number of JIS
	characters. The 'nlck' feature is used to access those
	glyphs.</p><p>Example: The glyph
          </p><div class="mediaobject"><img src="src/images/../../nlc1.gif"/></div><p>
	  is replaced by the glyph
          </p><div class="mediaobject"><img src="src/images/../../nlc2.gif"/></div><p>.</p><p>Recommended implementation: One-for-one substitution of
	non-NLC glyphs by the corresponding NLC glyph.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Used only with Kanji
	script.</p><p>Feature interaction: This feature is exclusive with the
	'jp78', 'jp83', 'jp90' and similar features. It can be
	combined with the 'palt', 'vpal', 'vert' and 'vrt2' features.</p><p>Tag: "nukt"</p><p>Friendly name: Nukta Forms</p><p>Registered by: Microsoft</p><p>Function: Produces Nukta forms in Indic scripts.</p><p>Example: In Hindi (Devanagari script), a consonant when
	combined with a nukta gives its nukta form.</p><p>Recommended implementation: The nukt table maps the
	sequence of a consonant followed by a nukta to the consonant's
	nukta form (GSUB lookup type 4).</p><p>Application interface: The application passes the
	sequence of GIDs (consonant and nukta), to the table, and gets
	back the GID for the nukta form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'numr'</p><p>Friendly name: Numerators</p><p>Registered by: Adobe</p><p>Function: Replaces selected figures which precede a
	slash with numerator figures, and replaces the typographic
	slash with the fraction slash.</p><p>Example: In the string 11/17 selected by the user, the
	application turns the 11 into numerators, and the slash into a
	fraction slash when the user applies the fraction feature
	(frac).</p><p>Recommended implementation: The numr table maps sets of
	figures and related characters to corresponding numerator
	glyphs in the font. It also maps the typographic slash
	(U+002F) to the fraction slash (U+2044). All mappings are
	one-to-one (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the numr
	coverage table, the application passes a GID to the table and
	gets back a new GID.</p><p>UI suggestion: This feature should normally be called by
	an application when the user applies the frac feature.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature supports frac. It may
	be used in combination with other substitution (GSUB)
	features, whose results it may override.</p><p>Tag: 'onum'</p><p>Friendly name: Oldstyle Figures</p><p>Registered by: Microsoft/Adobe</p><p>Function: This feature changes selected figures from the
	default lining style to oldstyle form.</p><p>Example: The user invokes this feature to get oldstyle
	figures, which fit better into the flow of normal upper- and
	lowercase text. Various characters designed to be used with
	figures may also have oldstyle versions.</p><p>Recommended implementation: The onum table maps each
	lining figure, and any associated characters, to the
	corresponding oldstyle form (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the onum
	coverage table, the application passes a GID to the onum table
	and gets back a new GID.</p><p>UI suggestion: Users can switch between the lining and
	oldstyle sets by turning this feature on or off. Note: This
	feature is separate from the figure-width features pnum and
	tnum. When the user changes figure style, the application may
	want to query whether a change in width is also desired.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature overrides the results
	of the Lining Figures feature (lnum).</p><p>Tag: 'opbd'</p><p>Friendly name: Optical Bounds</p><p>Registered by: Adobe (Modified by Adobe, this is the
	newer description)</p><p>Function: Aligns glyphs by their apparent left or right
	extents in horizontal setting, or apparent top or bottom
	extents in vertical setting, replacing the default behavior of
	aligning glyphs by their origins. Another name for this
	behavior would be visual justification. The optical edge of a
	given glyph is only indirectly related to its advance width or
	bounding box; this feature provides a means for getting true
	visual alignment.</p><p>Example: Succeeding lines beginning with T, D and W
	would shift to the left by varying amounts when the text is
	left-justified and this feature is applied. Succeeding lines
	ending with r, h and y would likewise shift to the right by
	differing degrees when the text is right-justified and this
	feature is applied.</p><p>Recommended implementation: Values for affected glyphs
	are defined with a separate record for left, right, top, and
	bottom. Each record describes the amount by which the
	placement and advance width should be altered (GPOS lookup
	type 1).</p><p>Application interface: For GIDs found in the opbd
	coverage table, the application calls one of two related
	tables, depending on the position of the glyph. For glyphs at
	the left end of a horizontal line, it calls the lfbd table,
	for glyphs at the right end of a horizontal line, it calls the
	rtbd table.</p><p>UI suggestion: This feature should be active by
	default. It effectively changes the line length, so
	justification algorithms should account for this adjustment.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: Should not be applied to glyphs
	which use fixed-width features (e.g. fwid, halt, hwid, qwid
	and twid) or vertical features (e.g. vert, vrt2, vpal, valt
	and vhal). Uses lfbd and rtbd features.</p><p>Tag: 'ordn'</p><p>Friendly name: Ordinals</p><p>Registered by: Adobe</p><p>Function: Replaces default alphabetic glyphs with the
	corresponding ordinal forms for use after figures. One
	exception to the follows-a-figure rule is the numero character
	(U+2116), which is actually a ligature substitution, but is
	best accessed through this feature.</p><p>Example: The user applies this feature to turn 2.o into
	2.o (abbreviation for secundo).</p><p>Recommended implementation: The ordn table maps various
	lowercase letters to corresponding ordinal forms in a chained
	context (GSUB lookup type 6), and the sequence No to the
	numero character (GSUB lookup type 4).</p><p>Application interface: For sets of GIDs found in the
	clig coverage table, the application passes the sequence of
	GIDs to the table and gets back new GIDs. Note that full
	sequences must be passed. Note: This may be a change of
	semantic value. Besides the original character codes, the
	application should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies mostly to Latin
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'ornm'</p><p>Friendly name: Ornaments</p><p>Registered by: Adobe</p><p>Function: This is a dual-function feature, which uses
	two input methods to give the user access to ornament glyphs
	(e.g. fleurons, dingbats and border elements) in the font. One
	method replaces the bullet character with a selection from the
	full set of available ornaments; the other replaces specific
	"lower ASCII" characters with ornaments assigned to them. The
	first approach supports the general or browsing user; the
	second supports the power user.</p><p>Example: The user inputs qwwwwwwwwwe to form the top of
	a flourished box in Adobe Caslon, or inputs the bullet
	character, then chooses the thistle dingbat.</p><p>Recommended implementation: The ornm table maps all
	ornaments in a font to the bullet character (GSUB lookup type
	3) and each ornament in a font to a corresponding alphanumeric
	character (GSUB lookup type 1). The manufacturer may choose to
	build two tables (one for each lookup type) or only one which
	uses lookup type 3 for all substitutions. As in any
	one-from-many substitution, alternates present in more than
	one face should be ordered consistently across a family, so
	that those alternates can work correctly when switching
	between family members.</p><p>Application interface: When this feature is invoked, the
	application must note whether the selected text is the bullet
	character (U+2022) or alphanumeric characters. In the first
	case, it passes the GID for bullet to the ornm table and gets
	back a set of GIDs, and gives the user a means to select from
	among them. In the second case, for GIDs found in the ornm
	coverage table, it passes GIDs to the ornm table and gets back
	new GIDs.</p><p>UI suggestion: This feature should be inactive by
	default. When more than one GID is returned (the bullet case),
	an application could display the forms sequentially in
	context, or present a palette showing all the forms at once,
	or give the user a choice between these approaches. Once the
	user has selected a specific ornament, that one should be the
	default selection the next time the bullet is typed. In the
	absence of such prior information, the application may assume
	that the first ornament in a set is the preferred form, so the
	font developer should order them accordingly.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature is mutually exclusive
	with all other substitution (GSUB) features, which should be
	turned off when it's applied.</p><p>Tag: 'palt'</p><p>Friendly name: Proportional Alternate Widths</p><p>Registered by: Adobe</p><p>Function: Respaces glyphs designed to be set on full-em
	widths, fitting them onto individual (more or less
	proportional) horizontal widths. This differs from pwid in
	that it does not substitute new glyphs (GPOS, not GSUB
	feature). The user may prefer the monospaced form, or may
	simply want to ensure that the glyph is well-fit and not
	rotated in vertical setting (Latin forms designed for
	proportional spacing would be rotated).</p><p>Example: The user may invoke this feature in a Japanese
	font to get Latin, Kanji, Kana or Symbol glyphs with the
	full-width design but individual metrics.</p><p>Recommended implementation: The font specifies alternate
	metrics for the full-width glyphs (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the palt
	coverage table, the application passes the GIDs to the table
	and gets back positional adjustments (XPlacement, XAdvance,
	YPlacement and YAdvance).</p><p>UI suggestion: This feature would be off by default.</p><p>Script/language sensitivity: Used mostly in CJKV fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. fwid, halt, hwid,
	qwid and twid), which should be turned off when it's
	applied. Applying this feature should activate the kern
	feature. See also vpal.</p><p>Tag:'pcap'</p><p>Friendly name: Petite Capitals</p><p>Registered by: Tiro Typeworks / Emigre</p><p>Function: Some fonts contain an additional size of
	capital letters, shorter than the regular smallcaps and
	whimsically referred to as petite caps. Such forms are most
	likely to be found in designs with a small lowercase x-height,
	where they better harmonise with lowercase text than the
	taller smallcaps (for examples of petite caps, see the Emigre
	type families Mrs Eaves and Filosofia). This feature turns
	lowercase characters into petite capitals. Forms related to
	petite capitals, such as specially designed figures, may be
	included.</p><div class="figure"><a name="idm483207936256"></a><p class="title"><strong>Figure 42.1. pcap illustration</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../pcapprop.gif" alt="pcap illustration"/></div></div></div><br class="figure-break"/><p/><p>Example: The user enters text as lowercase or mixed
	case, and gets petite cap text or text with regular uppercase
	and petite caps. Note that some designers, might extend the
	petite cap lookups to include uppercase-to-smallcap
	substitutions, creating a shifting hierarchy of uppercase
	forms.</p><p>Recommended implementation: The pcap table maps
	lowercase glyphs to the corresponding petite cap forms (GSUB
	lookup type 1).</p><p>Application interface: For GIDs found in the pcap
	coverage table, the application passes GIDs to the pcap table,
	and gets back new GIDs. Petite cap substitutions should follow
	language rules for smallcap (smcp) substitutions.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to scripts
	with both upper- and lowercase forms (e.g. Latin, Cyrillic,
	Greek).</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'pnum'</p><p>Friendly name: Proportional Figures</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces figure glyphs set on uniform
	(tabular) widths with corresponding glyphs set on
	glyph-specific (proportional) widths. Tabular widths will
	generally be the default, but this cannot be safely
	assumed. Of course this feature would not be present in
	monospaced designs.</p><p>Example: The user may apply this feature to get even
	spacing for lining figures used as dates in an all-cap
	headline.</p><p>Recommended implementation: In order to simplify
	associated kerning and get the best glyph design for a given
	width, this feature should use new glyphs for the figures,
	rather than only adjusting the fit of the tabular glyphs
	(although some may be simple copies); i.e. not a GPOS
	feature. The pnum table maps tabular versions of lining and/or
	oldstyle figures to corresponding proportional glyphs (GSUB
	lookup type 1).</p><p>Application interface: For GIDs found in the pnum
	coverage table, the application passes GIDs to the pnum table
	and gets back new GIDs.</p><p>UI suggestion: This feature should be off by
	default. The application may want to query the user about this
	feature when the user changes figure style (onum or lnum).</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature overrides the results
	of the Tabular Figures feature (tnum).</p><p>Tag: 'pref'</p><p>Friendly name: Pre-base Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the pre-base form of a consonant.</p><p>Example: In the Khmer script, the consonant Ra has a
	pre-base subscript form subscript called Coeng Ra. When the
	sequence of Coeng followed by Ra, its pre-base form is
	substituted.</p><p>Recommended implementation: The pref table maps the
	sequence required to convert a consonant into its pre-base
	form (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	pref table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the pre base form of the
	consonant.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Khmer and
	Myanmar (Burmese) scripts that have pre-base forms for
	consonants.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'pres'</p><p>Friendly name: Pre-base Substitutions</p><p>Registered by: Microsoft</p><p>Function: Produces the pre-base forms of conjuncts in
	Indic scripts. It can also be used to substitute the
	appropriate glyph variant for pre-base vowel signs.</p><p>Example: In the Gujarati (Indic) script, the doubling of
	consonant Ka requires the first Ka to be substituted by its
	pre-base form. This in turn ligates with the second
	Ka. Applying this feature would result in the ligaturised
	version of the doubled Ka.</p><p>Recommended implementation: The pres table maps a
	sequence of consonants separated by the virama (halant), to
	the ligated conjunct form (GSUB lookup type 4). In the case of
	pre-base matra substitution, the appropriate matra can be
	substituted using contextual substitution (GSUB lookup type
	5).</p><p>Application interface: For substitutions defined in the
	pres table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the ligature (or matra as
	the case may be).</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'pstf'</p><p>Friendly name: Post-base Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the post-base form of a
	consonant.</p><p>Example: In the Gurmukhi (Indic) script, the consonant
	Ya has a post base form. When the Ya is used as the second
	consonant in conjunct formation, its post-base form is
	substituted.</p><p>Recommended implementation: The pstf table maps the
	sequence required to convert a consonant into its post-base
	form (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	pstf table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the post base form of the
	consonant.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic scripts
	that have post-base forms for consonants eg: Gurmukhi,
	Malayalam.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'psts'</p><p>Friendly name: Post-base Substitutions</p><p>Registered by: Microsoft</p><p>Function: Substitutes a sequence of a base glyph and
	post-base glyph, with its ligaturised form.</p><p>Example: In the Malayalam (Indic) script, the consonant
	Va has a post base form. When the Va is doubled to form a
	conjunct- VVa; the first Va [base] and the post base form that
	follows it, is substituted with a ligature.</p><p>Recommended implementation: The psts table maps
	identified conjunct formation sequences to corresponding
	ligatures (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	psts table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the ligature.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Can be used in any
	alphabetic script. Required in Indic scripts.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'pwid'</p><p>Friendly name: Proportional Widths</p><p>Registered by: Adobe</p><p>Function: Replaces glyphs set on uniform widths
	(typically full or half-em) with proportionally spaced
	glyphs. The proportional variants are often used for the Latin
	characters in CJKV fonts, but may also be used for Kana in
	Japanese fonts.</p><p>Example: The user may invoke this feature in a Japanese
	font to get a proportionally-spaced glyph instead of a
	corresponding half-width Roman glyph or a full-width Kana
	glyph.</p><p>Recommended implementation: The font contains alternate
	glyphs designed to be set on proportional widths (GSUB lookup
	type 1).</p><p>Application interface: For GIDs found in the pwid
	coverage table, the application passes the GIDs to the table
	and gets back new GIDs.</p><p>UI suggestion: Applications may want to have this
	feature active or inactive by default depending on their
	markets.</p><p>Script/language sensitivity: Although used mostly in
	CJKV fonts, this feature could be applied in European
	scripts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. fwid, halt, hwid,
	palt, qwid, twid, valt and vhal), which should be turned off
	when it's applied. Applying this feature should activate the
	kern feature.</p><p>Tag: 'qwid'</p><p>Friendly name: Quarter Widths</p><p>Registered by: Adobe</p><p>Function: Replaces glyphs on other widths with glyphs
	set on widths of one quarter of an em (half an en). The
	characters involved are normally figures and some forms of
	punctuation.</p><p>Example: The user may apply qwid to place a four-digit
	figure in a single slot in a column of vertical text.</p><p>Recommended implementation: The font may contain
	alternate glyphs designed to be set on quarter-em widths (GSUB
	lookup type 1), or it may specify alternate metrics for the
	original glyphs (GPOS lookup type 1) which adjust their
	spacing to fit in quarter-em widths.</p><p>Application interface: For GIDs found in the qwid
	coverage table, the application passes the GIDs to the table
	and gets back either new GIDs or positional adjustments
	(XPlacement and XAdvance).</p><p>UI suggestion: This feature would normally be off by
	default.</p><p>Script/language sensitivity: Generally used only in CJKV
	fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. fwid, halt, hwid and
	twid), which should be turned off when it's applied. It
	deactivates the kern feature.</p><p>Tag: 'rand'</p><p>Friendly name: Randomize</p><p>Registered by: Adobe</p><p>Function: In order to emulate the irregularity and
	variety of handwritten text, this feature allows multile
	alternate forms to be used.</p><p>Example: The user applies this feature in FF Kosmic to
	get three forms of f in one word.</p><p>Recommended implementation: The rand table maps GIDs for
	default glyphs to one or more GIDs for corresponding
	alternates (GSUB lookup type 3).</p><p>Application interface: For GIDs found in the rand
	coverage table, the application passes a GID to the rand table
	and gets back one or more new GIDs. The application selects
	one of these either by a pseudo-random algorithm, or by noting
	the sequence of IDs returned, storing that sequence, and
	stepping through that set as the corresponding character code
	is invoked.</p><p>UI suggestion: This feature should be enabled/disabled
	via a preference setting; "enabled" is the recommended
	default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'rlig'</p><p>Friendly name: Required Ligatures</p><p>Registered by: Microsoft</p><p>Function: Replaces a sequence of glyphs with a single
	glyph which is preferred for typographic purposes. This
	feature covers those ligatures, which the script determines as
	required to be used in normal conditions. This feature is
	important for some scripts to insure correct glyph formation.</p><p>Example: The Arabic character lam followed by alef will
	always form a ligated lamalef form. This ligated form is a
	requirement of the script's shaping. The same happens with the
	Syriac script.</p><p>Recommended implementation: The rlig table maps GIDs for
	default glyphs to one or more GIDs for corresponding
	alternates (GSUB lookup type 3).</p><p>Application interface: The rlig table maps sequences of
	glyphs to corresponding ligatures (GSUB lookup type
	4). Ligatures with more components must be stored ahead of
	those with fewer components in order to be found. The set of
	standard ligatures will normally remain constant by script.</p><p>UI suggestion: This feature should be active by
	default. It is recommended that this feature not be turned off
	to avoid breaking obligatory script shaping.</p><p>Script/language sensitivity: Applies to Arabic and
	Syriac. May apply to some other scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. See also liga.</p><p>Tag: 'rphf'</p><p>Friendly name: Reph Form</p><p>Registered by: Microsoft</p><p>Function: Substitutes the Reph form for a consonant and
	halant sequence.</p><p>Example: In the Devanagari (Indic) script, the consonant
	Ra possesses a reph form. When the Ra is a syllable initial
	consonant and is followed by the virama, it is repositioned
	after the post base vowel sign within the syllable, and also
	substituted with a mark that sits above the base glyph.</p><p>Recommended implementation: The rphf table maps the
	sequence of default form of Ra and virama to the Reph (GSUB
	lookup type 4).</p><p>Application interface: The application gets back the GID
	for the reph mark.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic
	scripts. eg: Devanagari, Kannada.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'rtbd'</p><p>Friendly name: Right Bounds</p><p>Registered by: Adobe</p><p>Function: Aligns glyphs by their apparent right extents
	at the right ends of horizontal lines of text, replacing the
	default behavior of aligning glyphs by their origins. This
	feature is called by the Optical Bounds (opbd) feature above.</p><p>Example: Succeeding lines ending with r, h and y would
	shift to the right by differing degrees when the text is
	right-justified and this feature is applied.</p><p>Recommended implementation: Values for affected glyphs
	describe the amount by which the placement and advance width
	should be altered (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the rtbd
	coverage table, the application passes a GID to the table and
	gets back a new XPlacement and XAdvance value.</p><p>UI suggestion: This feature is called by an application
	when the user invokes the opbd feature.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: Should not be applied to glyphs
	which use fixed-width features (e.g. fwid, halt, hwid, qwid
	and twid) or vertical features (e.g. vert, vrt2, vpal, valt
	and vhal). Is called by opbd feature.</p><p>Tag: 'rtla'</p><p>Friendly name: Right-to-left alternates</p><p>Registered by: Adobe</p><p>Function: A number of Unicode characters are rendered by
	different shapes depending on the directional context in which
	they appear. For example, the character U+0028 LEFT
	PARENTHESIS is interpreted by the Unicode standard as an
	opening parenthesis and it appears as "(" in left-to-right
	contexts, and as ")" in right-to-left contexts (this is
	described on page 66 of the Unicode Standard, version
	3.0). The 'rtla' feature is used to access the shape
	appropriate for a right-to-left context.</p><p>Example: The 'rtla' feature replaces the glyph "(" by
	the glyph ")".</p><p>Recommended implementation: These are one-to-one
	substitutions (GSUB lookup type 1). Since this feature is a
	glyph selection feature, it should probably be performed early
	in the shaping process. At least all the glyphs mapped from
	characters with the mirrored property should have a
	replacement.</p><p>Application interface: The layout application applies
	the Unicode bidi algorithm to the character string to display,
	and maps the resulting character string to glyphs via the
	cmap. It activates the 'rtla' feature on glyphs that
	correspond to characters with an odd (right-to-left) resolved
	level. It is important to note that this feature can be
	applied to more glyphs than those that correspond to
	characters with the mirrored property. The motivation is that
	the font designer may want additional characters to assume
	different shapes.</p><p>If the 'rtla' feature is implemented, it must be
	implemented for all glyphs in the font that represent Unicode
	characters with the mirrored property. If the 'rtla' feature
	is not implemented, it is assumed that the application will
	take care of bidirectional mirroring through an algorithm.</p><p>UI suggestion: None.</p><p>Script/language sensitivity: Scripts that are
	right-to-left.</p><p>Feature interaction: This feature may be used in
	combination with other features.</p><p>Tag: 'ruby'</p><p>Friendly name: Ruby Notation Forms</p><p>Registered by: Adobe</p><p>Function: Japanese typesetting often uses smaller kana
	glyphs, generally in superscripted form, to clarify the
	meaning of kanji which may be unfamiliar to the reader. These
	are called ruby, from the old typesetting term for
	four-point-sized type. This feature identifies glyphs in the
	font which have been designed for this use, substituting them
	for the default designs.</p><p>Example: The user applies this feature to the kana
	character U+3042, to get the ruby form for annotation.</p><p>Recommended implementation: The font contains alternate
	glyphs for all kana characters which are enabled for ruby
	notation. The ruby table maps GIDs for default forms to GIDs
	for corresponding ruby alternates. These are one-to-one
	substitutions (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the ruby
	coverage table, the application passes the GIDs for default
	forms to the table and gets back new GIDs for ruby forms. The
	application then scales and positions these forms according to
	its defaults, which may take user parameters.</p><p>UI suggestion: This feature should be inactive by
	default. Applications may offer the user an opportunity to
	specify the degree of scaling and baseline shift.</p><p>Script/language sensitivity: Applies only to Japanese.</p><p>Feature interaction: This feature overrides the results
	of any other feature for the affected characters.</p><p>Tag: 'salt'</p><p>Friendly name: Stylistic Alternates</p><p>Registered by: Adobe</p><p>Function: Many fonts contain alternate glyph designs for
	a purely esthetic effect; these do not always fit into a clear
	category like swash or historical. As in the case of swash
	glyphs, there may be more than one alternate form. This
	feature replaces the default forms with the stylistic
	alternates.</p><p>Example: The user applies this feature to Industria to
	get the alternate form of g.</p><p>Recommended implementation: The salt table maps GIDs for
	default forms to one or more GIDs for corresponding stylistic
	alternatives. While many of these substitutions are one-to-one
	(GSUB lookup type 1), others require a selection from a set
	(GSUB lookup type 3). The manufacturer may choose to build two
	tables (one for each lookup type) or only one which uses
	lookup type 3 for all substitutions. As in any one-from-many
	substitution, alternates present in more than one face should
	be ordered consistently across a family, so that those
	alternates can work correctly when switching between family
	members.</p><p>Application interface: For GIDs found in the salt
	coverage table, the application passes the GIDs to the salt
	table and gets back one or more new GIDs. If more than one GID
	is returned, the application must provide a means for the user
	to select the one desired.</p><p>UI suggestion: This feature should be inactive by
	default. When more than one GID is returned, an application
	could display the forms sequentially in context, or present a
	palette showing all the forms at once, or give the user a
	choice between these approaches. The application may assume
	that the first glyph in a set is the preferred form, so the
	font developer should order them accordingly.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'sinf'</p><p>Friendly name: Scientific Inferiors</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces lining or oldstyle figures with
	inferior figures (smaller glyphs which sit lower than the
	standard baseline, primarily for chemical or mathematical
	notation). May also replace lowercase characters with
	alphabetic inferiors.</p><p>Example: The application can use this feature to
	automatically access the inferior figures (more legible than
	scaled figures).</p><p>Recommended implementation: The sinf table maps figures
	to the corresponding inferior forms (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the sinf
	coverage table, the application passes a GID to the feature
	and gets back a new GID.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Can apply to nearly any
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'size'</p><p>Friendly name: Optical size</p><p>Registered by: Adobe</p><p>Function: This feature stores two kinds of information
	about the optical size of the font: design size (the point
	size for which the font is optimized) and size range (the
	range of point sizes which the font can serve well), as well
	as other information which helps applications use the size
	range. The design size is useful for determining proper
	tracking behavior. The size range is useful in families which
	have fonts covering several ranges. Additional values serve to
	identify the set of fonts which share related size ranges, and
	to identify their shared name. Note that sizes refer to
	nominal final output size, and are independent of viewing
	magnification or resolution.</p><p>Required implementation:</p><p>The Feature table of this GPOS feature contains no
	lookups; its Feature Parameters field records an offset from
	the beginning of the Feature table to an array of five 16-bit
	unsigned integer values. The size feature must be implemented
	in all fonts in any family which uses the feature. In this
	usage, a family is a set of fonts which share a Preferred
	Family name (name ID 16), or Font Family name (name ID 1) if
	the Preferred Family name is absent.</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The first value represents the design size in
	      720/inch units (decipoints). The design size entry must
	      be non-zero. When there is a design size but no
	      recommended size range, the rest of the array will
	      consist of zeros.</p></li><li class="listitem"><p>The second value has no independent meaning, but
	    serves as an identifier that associates fonts in a
	    subfamily. All fonts which share a Preferred or Font
	    Family name and which differ only by size range shall have
	    the same subfamily value, and no fonts which differ in
	    weight or style shall have the same subfamily value. If
	    this value is zero, the remaining fields in the array will
	    be ignored.</p></li><li class="listitem"><p>The third value enables applications to use a single
	      name for the subfamily identified by the second
	      value. If the preceding value is non-zero, this value
	      must be set in the range 256 - 32767 (inclusive). It
	      records the value of a field in the name table, which
	      must contain English-language strings encoded in Windows
	      Unicode and Macintosh Roman, and may contain additional
	      strings localized to other scripts and languages. Each
	      of these strings is the name an application should use,
	      in combination with the family name, to represent the
	      subfamily in a menu. Applications will choose the
	      appropriate version based on their selection criteria.</p></li><li class="listitem"><p>The fourth and fifth values represent the small end
	    of the recommended usage range (exclusive) and the large
	    end of the recommended usage range (inclusive), stored in
	    720/inch units (decipoints). Ranges must not overlap, and
	    should generally be contiguous.</p></li></ul></div><p>Example: The size information in Bell Centennial is [60
	0 0 0 0]. This tells an application that the font's design
	size is six points, so larger sizes may need proportionate
	reduction in default inter-glyph spacing. The size information
	in Minion Pro Semibold Condensed Subhead is [180 3 257 139
	240]. These values tell an application that:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The font’s design size is 18 points;</p></li><li class="listitem"><p>This font is part of a subfamily of fonts that
	    differ only by the size range which each covers, and which
	    share the arbitrary identifier number 3;</p></li><li class="listitem"><p>ID 257 in the name table is the suggested menu name
	    for this subfamily. In this case, the string at name ID
	    257 is Semibold Condensed;</p></li><li class="listitem"><p>This font is the recommended choice from sizes
	    greater than 13.9-point up through 24-points.</p></li></ul></div><p>Application interface: When the user specifies a size,
	the application checks for a size feature in the active
	font. If none is found, the application follows its default
	behavior. If one is found, the application follows the
	specified offset to retrieve the five values.</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Design size: Applications which offer size-based
	    tracking have a pre-defined curve which they can apply. By
	    default, this curve should be set to produce no adjustment
	    at the font's design size (first value in the array, in
	    decipoints).</p></li><li class="listitem"><p>Size ranges: If the second value in the size array
	    is non-zero, the font has a recommended size range. When
	    any such font is selected by the user, the application
	    builds a list of all fonts with this subfamily value and
	    the same Preferred Family name, and notes the size range
	    in the current font. Applications may want to cache the
	    subfamily list at this point. If the specified size falls
	    in the current font's range, the application uses the
	    current font. If not, the application checks the other
	    ranges in the subfamily, and if the specified size falls
	    in one of them, uses that font. If the specified size is
	    not in any range present, the font with the range closest
	    to the specified value is used. If the specified size
	    falls exactly between two ranges, the range with the
	    larger values is used. Since adding or removing fonts from
	    a subfamily may cause reflow, applications should note
	    which fonts are used for which text.</p></li></ul></div><p>UI suggestion: This feature should be active by
	default. Applications may want to present the tracking curve
	to the user for adjustments via a GUI. At start-up, and when
	fonts are added or removed, applications may want to build a
	list of fonts with such ranges, and display the filtered
	subfamily names in their font selection UI, with each filtered
	name representing the full set of related sizes. Applications
	may also present a setting which allows the user to select
	non-default sizes (for example, in the case where final output
	is intended for on-screen viewing, a smaller optical size will
	produce better results). In such a case, the font-selection UI
	should present the unfiltered names. Applications should
	notify the user if fonts are removed or added from a subfamily
	with size ranges, and query about desired behavior.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: None.</p><p>Tag: 'smcp'</p><p>Friendly name: Small Capitals</p><p>Registered by: Microsoft/Adobe</p><p>Function: This feature turns lowercase characters into
	small capitals. This corresponds to the common SC font
	layout. It is generally used for display lines set in Large and
	small caps, such as titles. Forms related to small capitals,
	such as oldstyle figures, may be included.</p><p>Example: The user enters text as mixed capitals and
	lowercase, and gets Large and small cap text.</p><p>Recommended implementation: The smcp table maps
	lowercase glyphs to the corresponding small-cap forms (GSUB
	lookup type 1).</p><p>Application interface: For GIDs found in the smcp
	coverage table, the application passes GIDs to the smcp table,
	and gets back new GIDs. Note that applications should treat ß
	(U+00DF) as a pair of s characters, and that the Turkish
	dotless i maps to the normal small cap I.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to European
	scripts (Cyrillic, Greek and Latin), which have capital forms.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. Also see c2sc.</p><p>Tag: 'smpl'</p><p>Friendly name: Simplified Forms</p><p>Registered by: Adobe</p><p>Function: Replaces 'traditional' Chinese or Japanese
	forms with the corresponding 'simplified' forms.</p><p>Example: The user gets U+53F0 when U+6AAF, U+81FA, or
	U+98B1 is entered.</p><p>Recommended implementation: The smpl table maps each
	traditional form in a font to a corresponding simplified form
	(GSUB lookup type 1). Note that more than one traditional form
	may map to a single simplified form.</p><p>Application interface: For GIDs found in the smpl
	coverage table, the application passes the GIDs to the table
	and gets back one new GID for each. Note: This is a change of
	character code. Besides the original character code, the
	application should store the code for the new character.</p><p>UI suggestion: This feature would be off by default, but
	could be made the default by a preference setting.</p><p>Script/language sensitivity: Applies only to Chinese and
	Japanese.</p><p>Feature interaction: This feature is mutually exclusive
	with all other features, which should be turned off when
	it is applied, except the palt, vert and vrt2 features,
	which may be used in addition; trad and tnam are mutally
	exclusive, and override the results of smpl.</p><p>Tag: 'ss01' - 'ss20'</p><p>Friendly name: Stylistic Set 1 - Stylistic Set 20</p><p>Registered by: Tiro Typeworks</p><p>Function: In addition to, or instead of, stylistic
	alternatives of individual glyphs (see 'salt' feature), some
	fonts may contain sets of stylistic variant glyphs
	corresponding to portions of the character set, e.g. multiple
	variants for lowercase letters in a Latin font. Glyphs in
	stylistic sets may be designed to harmonise visually,
	interract in particular ways, or otherwise work
	together. Examples of fonts including stylistic sets are
	Zapfino Linotype and Adobe's Poetica. Individual features
	numbered sequentially with the tag name convention 'ss01'
	'ss02' 'ss03' . 'ss20' provide a mechanism for glyphs in these
	sets to be associated via GSUB lookup indexes to default forms
	and to each other, and for users to select from available
	stylistic sets.</p><p>Recommended implementation: An ssXX table maps GIDs for
	default forms to one GIDs for corresponding stylistic
	alternatives in each set. Each ssXX feature uses one-to-one
	(GSUB lookup type 1) substitutions. Font developers may choose
	to map only from default forms to variants for each stylistic
	set, or may choose to map between all stylistic sets in each
	feature, depending on intended user experience. For example,
	feature 'ss03' might contain lookups mapping variant glyphs
	from 'ss01' and 'sso2' to corresponding variants in 'ss03', in
	addition to mapping from default forms.</p><p>Application interface: Note that the application is
	responsible for counting and enumerating the number of
	features in the font with tag names of the format 'ss01' to
	'ss20', and for presenting the user with an appropriate
	selection mechanism. For GIDs found in the ssXX coverage
	table, the application passes the GIDs to the ssXX table and
	gets back one or more new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override. Note that after an ssXX feature has
	been applied, the user may wish to apply glyph-specific
	features, e.g. 'salt', to individual glyphs in the resulting
	layout; font developers are responsible for ordering
	substitution lookups to obtain desired user experience.</p><p>Tag: 'subs'</p><p>Friendly name: Subscript</p><p>Registered by: Microsoft/Adobe</p><p>Function: The "subs" feature may replace a default glyph
	with a subscript glyph, or it may combine a glyph substitution
	with positioning adjustments for proper placement.</p><p>Recommended implementation: First, a single or
	contextual substitution lookup implements the subscript glyph
	(GSUB lookup type 1). Then, if the glyph needs repositioning,
	an application may apply a single adjustment, pair adjustment,
	or contextual adjustment positioning lookup to modify its
	position.</p><p>Application interface: For GIDs found in the subs
	coverage table, the application passes a GID to the feature
	and gets back a new GID. Note: This is a change of semantic
	value. Besides the original character codes, the application
	should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Can apply to nearly any
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'sups'</p><p>Friendly name: Superscript</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces lining or oldstyle figures with
	superior figures (primarily for footnote indication), and
	replaces lowercase letters with superior letters (primarily
	for abbreviated French titles).</p><p>Example: The application can use this feature to
	automatically access the superior figures (more legible than
	scaled figures) for footnotes, or the user can apply it to
	Mssr to get the classic form.</p><p>Recommended implementation: The sups table maps figures
	and lowercase letters to the corresponding superior forms
	(GSUB lookup type 1).</p><p>Application interface: For GIDs found in the sups
	coverage table, the application passes a GID to the feature
	and gets back a new GID. Note: This can include a change of
	semantic value. Besides the original character codes, the
	application should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Can apply to nearly any
	script.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'swsh'</p><p>Friendly name: Swash</p><p>Registered by: Microsoft/Adobe</p><p>Function: This feature replaces default character glyphs
	with corresponding swash glyphs. Note that there may be more
	than one swash alternate for a given character.</p><p>Example: The user inputs the ampersand character when
	setting text with Poetica with this feature active, and is
	presented with a choice of the 63 ampersand forms in that
	face.</p><p>Recommended implementation: The swsh table maps GIDs for
	default forms to those for one or more corresponding swash
	forms. While many of these substitutions are one-to-one (GSUB
	lookup type 1), others require a selection from a set (GSUB
	lookup type 3). The manufacturer may choose to build two
	tables (one for each lookup type) or only one which uses
	lookup type 3 for all substitutions. If several styles of
	swash are present across the font, the set of forms for each
	character should be ordered consistently.</p><p>Application interface: For GIDs found in the swsh
	coverage table, the application passes the GIDs to the swsh
	table and gets back one or more new GIDs. If more than one GID
	is returned, the application must provide a means for the user
	to select the one desired.</p><p>UI suggestion: This feature should be inactive by
	default. When more than one GID is returned, an application
	could display the forms sequentially in context, or present a
	palette showing all the forms at once, or give the user a
	choice between these approaches. The application may assume
	that the first glyph in a set is the preferred form, so the
	font developer should order them accordingly.</p><p>Script/language sensitivity: Does not apply to
	ideographic scripts.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'titl'</p><p>Friendly name: Titling</p><p>Registered by: Adobe</p><p>Function: This feature replaces the default glyphs with
	corresponding forms designed specifically for titling. These
	may be all-capital and/or larger on the body, and adjusted for
	viewing at larger sizes.</p><p>Example: The user applies this feature in Adobe Garamond
	to get the titling caps.</p><p>Recommended implementation: The titl table maps default
	forms to corresponding titling forms (GSUB lookup type 1).</p><p>Application interface: For GIDs found in the titl
	coverage table, the application passes the GIDs to the titl
	table and gets back new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'tjmo'</p><p>Friendly name: Trailing Jamo Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the trailing jamo form of a
	cluster.</p><p>Example: In Hangul script, the jamo cluster is composed
	of three parts (leading consonant, vowel, and trailing
	consonant). When a sequence of trailing class jamos are found,
	their combined trailing jamo form is substituted.</p><p>Recommended implementation: The tjmo table maps the
	sequence required to convert a series of jamos into its
	trailing jamo form (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	tjmo table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the trailing jamo form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required for Hangul script
	when Ancient Hangul writing system is supported.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'tnam'</p><p>Friendly name: Traditional Name Forms</p><p>Registered by: Adobe</p><p>Function: Replaces 'simplified' Japanese kanji forms
	with the corresponding 'traditional' forms. This is equivalent
	to the Traditional Forms feature, but explicitly limited to
	the traditional forms considered proper for use in personal
	names (as many as 205 glyphs in some fonts).</p><p>Example: The user inputs U+4E9C and gets U+4E9E.</p><p>Recommended implementation: The tnam table maps
	simplified forms in a font to corresponding traditional forms
	which can be used in personal names (GSUB lookup type 1). The
	application stores a record of any simplified forms which
	resulted from substitutions (the smpl feature); for such
	forms, applying the tnam feature undoes the previous
	substitution.</p><p>Application interface: For GIDs found in the tnam
	coverage table, the application passes the GIDs to the table
	and gets back new GIDs. Note: This is a change of character
	code. Besides the original character code, the application
	should store the code for the new character.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to Japanese.</p><p>Feature interaction: May include some characters
	affected by the Proportional Alternate Widths feature (palt);
	trad and tnam are mutually exclusive, and override the results
	of smpl.</p><p>Tag: 'tnum'</p><p>Friendly name: Tabular Figures</p><p>Registered by: Adobe</p><p>Function: Replaces figure glyphs set on proportional
	widths with corresponding glyphs set on uniform (tabular)
	widths. Tabular widths will generally be the default, but this
	cannot be safely assumed. Of course this feature would not be
	present in monospaced designs.</p><p>Example: The user may apply this feature to get oldstyle
	figures to align vertically in a column.</p><p>Recommended implementation: In order to simplify
	associated kerning and get the best glyph design for a given
	width, this feature should use new glyphs for the figures,
	rather than only adjusting the fit of the proportional glyphs
	(although some may be simple copies); i.e. not a GPOS
	feature. The tnum table maps proportional versions of lining
	and/or oldstyle figures to corresponding tabular glyphs (GSUB
	lookup type 1).</p><p>Application interface: For GIDs found in the tnum
	coverage table, the application passes GIDs to the tnum table
	and gets back new GIDs.</p><p>UI suggestion: This feature should be off by
	default. The application may want to query the user about this
	feature when the user changes figure style (onum or lnum).</p><p>Script/language sensitivity: None.</p><p>Feature interaction: This feature overrides the results
	of the Proportional Figures feature ( pnum).</p><p>Tag: 'trad'</p><p>Friendly name: Traditional Forms</p><p>Registered by: Adobe</p><p>Function: Replaces 'simplified' Chinese hanzi or
	Japanese kanji forms with the corresponding 'traditional'
	forms.</p><p>Example: The user inputs U+53F0 and is offered a choice
	of U+6AAF, U+81FA, or U+98B1.</p><p>Recommended implementation: The trad table maps each
	simplified form in a font to one or more traditional
	forms. While many of these substitutions are one-to-one (GSUB
	lookup type 1), others require a selection from a set (GSUB
	lookup type 3). The manufacturer may choose to build two
	tables (one for each lookup type) or only one which uses
	lookup type 3 for all substitutions. As in any one-from-many
	substitution, alternates present in more than one face should
	be ordered consistently across a family, so that those
	alternates can work correctly when switching between family
	members.</p><p>Application interface: For GIDs found in the trad
	coverage table, the application passes the GIDs to the table
	and gets back one or more new GIDs. If more than one GID is
	returned, the application must provide a means for the user to
	select the one desired. The application stores a record of any
	simplified forms which resulted from substitutions (the smpl
	feature); for such forms, applying the trad feature undoes the
	previous substitution. Note: This is a change of character
	code. Besides the original character code, the application
	should store the code for the new character.</p><p>UI suggestion: This feature should be inactive by
	default. If there's no record of a conversion from traditional
	to simplified, the user must be offered a set of possibilities
	from which to select. The application may note the user's
	choice, and offer it as a default the next time the source
	simplified character is encountered. In the absence of such
	prior information, the application may assume that the first
	glyph in a set is the preferred form, so the font developer
	should order them accordingly.</p><p>Script/language sensitivity: Applies only to Chinese and
	Japanese.</p><p>Feature interaction: May include some characters
	affected by the Proportional Alternate Widths feature (palt);
	trad and tnam are mutually exclusive, and override the results
	of smpl.</p><p>Tag: 'twid'</p><p>Friendly name: Third Widths</p><p>Registered by: Adobe</p><p>Function: Replaces glyphs on other widths with glyphs
	set on widths of one third of an em. The characters involved
	are normally figures and some forms of punctuation.</p><p>Example: The user may apply twid to place a three-digit
	figure in a single slot in a column of vertical text.</p><p>Recommended implementation: The font may contain
	alternate glyphs designed to be set on third-em widths (GSUB
	lookup type 1), or it may specify alternate metrics for the
	original glyphs (GPOS lookup type 1) which adjust their
	spacing to fit in third-em widths.</p><p>Application interface: For GIDs found in the twid
	coverage table, the application passes the GIDs to the table
	and gets back either new GIDs or positional adjustments
	(XPlacement and XAdvance).</p><p>UI suggestion: This feature would normally be off by
	default.</p><p>Script/language sensitivity: Generally used only in CJKV
	fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-width features (e.g. fwid, halt, hwid and
	qwid), which should be turned off when it's applied. It
	deactivates the kern feature.</p><p>Tag: 'unic'</p><p>Friendly name: Unicase</p><p>Registered by: Tiro Typeworks / Emigre</p><p>Function: This feature maps upper- and lowercase letters
	to a mixed set of lowercase and small capital forms, resulting
	in a single case alphabet (for an example of unicase, see the
	Emigre type family Filosofia). The letters substituted may
	vary from font to font, as appropriate to the design. If
	aligning to the x-height, smallcap glyphs may be substituted,
	or specially designed unicase forms might be
	used. Substitutions might also include specially designed
	figures.</p><div class="figure"><a name="idm483207770112"></a><p class="title"><strong>Figure 42.2. unic illustration</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../unicprop.gif" alt="unic illustration"/></div></div></div><br class="figure-break"/><p>Example: The user enters text as uppercase, lowercase or
	mixed case, and gets unicase text.</p><p>Recommended implementation: The unic table maps some
	uppercase and lowercase glyphs to corresponding unicase forms
	(GSUB lookup type 1).</p><p>Application interface: For GIDs found in the unic
	coverage table, the application passes GIDs to the unic table,
	and gets back new GIDs.</p><p>UI suggestion: This feature should be off by default.</p><p>Script/language sensitivity: Applies only to scripts
	with both upper- and lowercase forms (e.g. Latin, Cyrillic,
	Greek).</p><p>Feature interaction: This feature may be used in
	combination with other substitution (GSUB) features, whose
	results it may override.</p><p>Tag: 'valt'</p><p>Friendly name: Alternate Vertical Metrics</p><p>Registered by: Adobe (Modified by Adobe, this is the
	newer description)</p><p>Function: Repositions glyphs to visually center them
	within full-height metrics, for use in vertical
	setting. Typically applies to full-width Latin glyphs, which
	are aligned on a common horizontal baseline and not rotated
	when set vertically in CJKV fonts.</p><p>Example: Applying this feature would shift a Roman h
	down, or y up, from their default full-width positions.</p><p>Recommended implementation: The font specifies alternate
	metrics for the original glyphs (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the valt
	coverage table, the application passes the GIDs to the table
	and gets back positional adjustments (YPlacement).</p><p>UI suggestion: This feature should be active by default
	in vertical-setting contexts.</p><p>Script/language sensitivity: Applies only to scripts
	with vertical writing modes.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-height features (e.g. vhal and vpal),
	which should be turned off when it's applied. It deactivates
	the kern feature.</p><p>Tag: "vatu"</p><p>Friendly name: Vattu Variants</p><p>Registered by: Microsoft</p><p>Function: Substitutes ligatures for conjuncts made up of
	base consonants with consonants that have vattu forms.</p><p>Example: In the Devanagari (Indic) script, the consonant
	Ra takes a vattu form, when it is not the syllable initial
	consonant in a conjunct. This form ligates with the base
	consonant as well as half forms of consonants.</p><p>Recommended implementation: The vatu table maps
	consonant and vattu form combinations to their respective
	ligatures (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	vatu table, the application passes the sequence of GIDs to the
	table, and gets back the GID for the vattu variant ligature.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required in Indic
	scripts. eg: Devanagari.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'vert'</p><p>Friendly name: Vertical Alternates</p><p>Registered by: Microsoft/Adobe</p><p>Function: Replaces default forms with variants adjusted
	for vertical writing when in vertical writing mode. While most
	CJKV glyphs remain vertical when set in vertical writing mode,
	some take a different form (usually rotated and repositioned)
	for this purpose. Glyphs covered by this feature correspond to
	the set normally rotated in low-end DTP applications.</p><p>Example: In vertical writing mode, the opening
	parenthesis (U+FF08) is replaced by the rotated form
	(U+FE35).</p><p>Recommended implementation: The font includes rotated
	versions of the glyphs covered by this feature. The vert table
	maps the standard forms to the corresponding rotated forms
	(GSUB lookup type 1). This feature should be the last
	substitution in the font, and take input from other features.</p><p>Application interface: For GIDs found in the vert
	coverage table, the application passes GIDs to the feature,
	and gets back new GIDs. See the vrt2 feature description for
	more details.</p><p>UI suggestion: This feature should be active by default
	when vertical writing mode is on if the vrt2 feature is not
	present. See the vrt2 feature description for more details,
	and a discussion of vertical writing in CommonType.</p><p>Script/language sensitivity: Applies only to scripts
	with vertical writing capability.</p><p>Feature interaction: This is a subset of the vrt2
	feature; vrt2 is preferred. May be used in addition to any
	other feature.</p><p>Tag: 'vhal'</p><p>Friendly name: Alternate Vertical Half Metrics</p><p>Registered by: Adobe</p><p>Function: Respaces glyphs designed to be set on full-em
	heights, fitting them onto half-em heights. This differs from
	valt in that it does not substitute new glyphs.</p><p>Example: The user may invoke this feature in a CJKV font
	to get better fit for punctuation or symbol glyphs without
	disrupting the monospaced alignment.</p><p>Recommended implementation: The font specifies alternate
	metrics for the full-height glyphs (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the vhal
	coverage table, the application passes the GIDs to the table
	and gets back positional adjustments (XPlacement, XAdvance,
	YPlacement and YAdvance).</p><p>UI suggestion: This feature would be off by default.</p><p>Script/language sensitivity: Used only in CJKV fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-height features (e.g. valt and vpal),
	which should be turned off when it is applied. It
	deactivates the kern feature. See also halt.</p><p>Tag: "vjmo"</p><p>Friendly name: Vowel Jamo Forms</p><p>Registered by: Microsoft</p><p>Function: Substitutes the vowel jamo form of a cluster.</p><p>Example: In Hangul script, the jamo cluster is composed
	of three parts (leading consonant, vowel, and trailing
	consonant). When a sequence of vowel class jamos are found,
	their combined vowel jamo form is substituted.</p><p>Recommended implementation: The vjmo table maps the
	sequence required to convert a series of jamos into its vowel
	jamo form (GSUB lookup type 4).</p><p>Application interface: For substitutions defined in the
	vjmo table, the application passes the sequence of GIDs to the
	feature, and gets back the GID for the vowel jamo form.</p><p>UI suggestion: This feature should be on by default.</p><p>Script/language sensitivity: Required for Hangul script
	when Ancient Hangul writing system is supported.</p><p>Feature interaction: This feature overrides the results
	of all other features.</p><p>Tag: 'vkna'</p><p>Friendly name: Vertical Kana Alternates</p><p>Registered by: Adobe</p><p>Function: Replaces standard kana with forms that have
	been specially designed for only vertical writing. This is a
	typographic optimization for improved fit and more even
	color. Also see hkna.</p><p>Example: Standard full-width kana (hiragana and
	katakana) are replaced by forms that are designed for vertical
	use.</p><p>Recommended implementation: The font includes a set of
	specially-designed glyphs, listed in the vkna coverage
	table. The vkna feature maps the standard full-width forms to
	the corresponding special vertical forms (GSUB lookup type
	1).</p><p>Application interface: For GIDs found in the vkna
	coverage table, the application passes GIDs to the feature,
	and gets back new GIDs.</p><p>UI suggestion: This feature would be off by default.</p><p>Script/language sensitivity: Applies only to fonts that
	support kana (hiragana and katakana).</p><p>Feature interaction: Since this feature is only for
	vertical use, features applying to horizontal behaviors
	(e.g. kern) do not apply.</p><p>Tag: 'vkrn'</p><p>Friendly name: Vertical Kerning</p><p>Registered by: Adobe</p><p>Function: Adjusts amount of space between glyphs,
	generally to provide optically consistent spacing between
	glyphs. Although a well-designed typeface has consistent
	inter-glyph spacing overall, some glyph combinations require
	adjustment for improved legibility. Besides standard
	adjustment in the vertical direction, this feature can supply
	size-dependent kerning data via device tables, "cross-stream"
	kerning in the X text direction, and adjustment of glyph
	placement independent of the advance adjustment. Note that
	this feature may apply to runs of more than two glyphs, and
	would not be used in monospaced fonts. Also note that this
	feature applies only to text set vertically.</p><p>Example: When the katakana character U+30B9 or U+30D8 is
	followed by U+30C8 in a vertical setting, U+30C8 is shifted up
	to fit more evenly.</p><p>Recommended implementation: The font stores a set of
	adjustments for pairs of glyphs (GPOS lookup type 2 or
	8). These may be stored as one or more tables matching left
	and right classes, and/or as individual pairs. Additional
	adjustments may be provided for larger sets of glyphs
	(e.g. triplets, quadruplets, etc.) to overwrite the results of
	pair kerns in particular combinations.</p><p>Application interface: The application passes a sequence
	of GIDs to the kern table, and gets back adjusted positions
	(XPlacement, XAdvance, YPlacement and YAdvance) for those
	GIDs. When using the type 2 lookup on a run of glyphs, it's
	critical to remember to not consume the last glyph, but to
	keep it available as the first glyph in a subsequent run (this
	is a departure from normal lookup behavior).</p><p>UI suggestion: This feature should be active by default
	for vertical text setting. Applications may wish to allow
	users to add further manually-specified adjustments to suit
	specific needs and tastes.</p><p>Script/language sensitivity: None</p><p>Feature interaction: If 'vkrn' is activated, 'vpal' must
	also be activated if it exists. (If 'vpal' is activated, there
	is no requirement that 'vkrn' must also be activated.) May be
	used in addition to any other feature except those which
	result in fixed (uniform) advance heights.</p><p>Tag: 'vpal'</p><p>Friendly name: Proportional Alternate Vertical Metrics</p><p>Registered by: Adobe</p><p>Function: Respaces glyphs designed to be set on full-em
	heights, fitting them onto individual (more or less
	proportional) vertical heights. This differs from valt in that
	it does not substitute new glyphs (GPOS, not GSUB
	feature). The user may prefer the monospaced form, or may
	simply want to ensure that the glyph is well-fit.</p><p>Example: The user may invoke this feature in a Japanese
	font to get Latin, Kanji, Kana or Symbol glyphs with the
	full-height design but individual metrics.</p><p>Recommended implementation: The font specifies alternate
	heights for the full-height glyphs (GPOS lookup type 1).</p><p>Application interface: For GIDs found in the vpal
	coverage table, the application passes the GIDs to the table
	and gets back positional adjustments (XPlacement, XAdvance,
	YPlacement and YAdvance).</p><p>UI suggestion: This feature would be off by default.</p><p>Script/language sensitivity: Used mostly in CJKV fonts.</p><p>Feature interaction: This feature is mutually exclusive
	with all other glyph-height features (e.g. valt and vhal),
	which should be turned off when it's applied. Applying this
	feature should activate the kern feature. See also palt.</p><p>Tag: 'vrt2'</p><p>Friendly name: Vertical Alternates and Rotation</p><p>Registered by: Adobe</p><p>Function: Replaces some fixed-width (half-, third- or
	quarter-width) or proportional-width glyphs (mostly Latin or
	katakana) with forms suitable for vertical writing (that is,
	rotated 90 degrees clockwise). Note that these are a superset
	of the glyphs covered in the vert table.</p><p>ATM/NT 4.1 and the Windows 2000 OTF driver impose the
	following requirements for an CommonType font with CFF outlines
	to be used for vertical writing: the vrt2 feature must be
	present in the GSUB table, it must comprises a single lookup
	of LookupType 1 and LookupFlag 0, and the lookup must have a
	single subtable. The predecessor feature, vert, is ignored.</p><p>A rotated glyph must be designed such that its top side
	  bearing and vertical advance as recorded in the Vertical
	  Metrics (<a class="link" href="chapter.vmtx.html" title="Chapter 39. vmtx - Vertical Metrics Table">vmtx</a>) table are identical to the
	  left side bearing and horizontal advance, respectively, of
	  the corresponding upright glyph as recorded in the
	  Horizontal Metrics (<a class="link" href="chapter.hmtx.html" title="Chapter 8. hmtx - Horizontal Metrics">hmtx</a>) table. (The
	  horizontal advance of the rotated glyph may be set to any
	  value, since the glyph is intended only for vertical writing
	  use. The vendor may however set it to head.unitsPerEm, to
	  prevent overlap during font proofing tests, for
	  example.)</p><p>Thus, proportional-width glyphs with rotated forms in
	the vrt2 feature will appear identically spaced in both
	vertical and horizontal writing. In order for kerning to
	produce identical results as well, developers must ensure that
	the Vertical Kerning (vkrn) feature record kern values between
	the rotated glyphs that are the same as kern values between
	their corresponding upright glyphs in the Kerning (kern)
	feature.</p><p>Example: Proportional- or half-width Latin and
	half-width katakana characters are rotated 90 degrees
	clockwise for vertical writing.</p><p>Recommended implementation: The font includes rotated
	versions of the glyphs covered by this feature. The vrt2 table
	maps the standard (horizontal) forms to the corresponding
	vertical (rotated) forms (GSUB lookup type 1). This feature
	should be the last substitution in the font, and take input
	from other features.</p><p>Application interface: For GIDs found in the vrt2
	coverage table, the application passes GIDs to the feature,
	and gets back new GIDs.</p><p>UI suggestion: This feature should be active by default
	when vertical writing mode is on, although the user must be
	able to override it.</p><p>Script/language sensitivity: Applies only to scripts
	with vertical writing capability.</p><p>Feature interaction: Overrides the vert (Vertical
	Writing) feature, which is a subset of this one. May be used
	in addition to any other feature.</p><p>Tag: 'zero'</p><p>Friendly name: Slashed Zero</p><p>Registered by: Adobe</p><p>Function: Some fonts contain both a default form of
	zero, and an alternative form which uses a diagonal slash
	through the counter. Especially in condensed designs, it can
	be difficult to distinguish between 0 and O (zero and capital
	O) in any situation where capitals and lining figures may be
	arbitrarily mixed. This feature allows the user to change from
	the default 0 to a slashed form.</p><p>Example: When setting labels, the user applies this
	feature to get the slashed 0.</p><p>Recommended implementation: The zero table maps the GIDs
	for the lining forms of zero to corresponding slashed forms
	(GSUB lookup type 1).</p><p>Application interface: For GIDs in the zero coverage
	table, the application passes a GID to the zero table and gets
	back a new GID.</p><p>UI suggestion: Optimally, the application would store
	this as a preference setting, and the user could use the
	feature to toggle back and forth between the two forms. Most
	applications will want the default setting to disable this
	feature.</p><p>Script/language sensitivity: Does not apply to scripts
	which use forms other than 0 for zero.</p><p>Feature interaction: Applies only to lining figures, so
	  is inactivated by oldstyle figure features (e.g. onum).</p></div></div></div>