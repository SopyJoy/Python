library(tm)

#Create a vector containing only the text
#text <- datatext
text <- readLines(file.choose())

# Create a Corpus
docs <- Corpus(VectorSource(text))

docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, stripWhitespace)

docs<- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeWords, stopwords("english"))
filstop <- c("akin","aking","ako","alin","am","amin","aming","ang","ano","anumang","apat","at","atin","ating","ay","bababa","bago","bakit","bawat","bilang","dahil","dalawa","dapat","din","dito","doon","gagawin","gayunman","ginagawa","ginawa","ginawang","gumawa","gusto","habang","hanggang","hindi","huwag","iba","ibaba","ibabaw","ibig","ikaw","ilagay","ilalim","ilan","inyong","isa","isang","itaas","ito","iyo","iyon","iyong","ka","kahit","kailangan","kailanman","kami","kanila","kanilang","kanino","kanya","kanyang","kapag","kapwa","karamihan","katiyakan","katulad","kaya","kaysa","ko","kong","kulang","kumuha","kung","laban","lahat","lamang","likod","lima","maaari","maaaring","maging","mahusay","makita","marami","marapat","masyado","may","mayroon","mga","minsan","mismo","mula","muli","na","nabanggit","naging","nagkaroon","nais","nakita","namin","napaka","narito","nasaan","ng","ngayon","ni","nila","nilang","nito","niya","niyang","noon","o","pa","paano","pababa","paggawa","pagitan","pagkakaroon","pagkatapos","palabas","pamamagitan","panahon","pangalawa","para","paraan","pareho","pataas","pero","pumunta","pumupunta","sa","saan","sabi","sabihin","sarili","sila","sino","siya","tatlo","tayo","tulad","tungkol","una","walang", "mahigit")
docs <- tm_map(docs, removeWords, "the")
docs <- tm_map(docs, removeWords, "mga")
docs <- tm_map(docs, removeWords, "ang")
docs <- tm_map(docs, removeWords, "applause")
docs <- tm_map(docs, removeWords, "natin")
docs <- tm_map(docs, removeWords, "will")


dtm <- TermDocumentMatrix(docs)
matrix <- as.matrix(dtm)
words <- sort(rowSums(matrix), decreasing = TRUE)
df <- data.frame(word = names(words), freq=words)
set.seed(1234)

#For Reproducibility
wordcloud(words = df$word, freq = df$freq,
          min.freq = 1, max.words = 200, random.order = FALSE,
          rot.per = 0.35, colors = brewer.pal(8, "Dark2"))
wordcloud2(data=df, size= 0.7, shape = 'diamond')
