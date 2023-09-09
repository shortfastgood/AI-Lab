# Prompt Engineering

## Zero-Shot Promting

For description see [Zero-Shot Prompting](https://www.promptingguide.ai/techniques/zeroshot)

## Automatic Reasoning and Tool-use (ART)

For description see [Automatic Reasoning and Tool-use (ART)](https://www.promptingguide.ai/techniques/art)

### ChatGPT

ChatGPT offers a function that uses the ART technique under the name of "advanced data analysis." This function can be activated through the "Settings & Beta" 
menu that appears when you click on the three dots at the bottom of the sidebar. Once the option is activated, a new chat of the type "advanced data analysis" 
is created. In the prompt line, the + symbol appears, which, when selected, allows you to upload one or more files into the chat.

At this point, it is necessary to formulate a request that leads to the processing of the uploaded data. Once sent, ChatGPT generates an ad-hoc Python program 
that is executed. If the outcome is positive, the chat provides a link to download the result; otherwise, it proceeds with error correction. In the end, 
it is also possible to download the generated Python code.

The chat has access to the entire standard library of Python. To use ART, there's no need for Python programming knowledge, 
but those who have it can influence the chat's decisions.

### Image Processing with ChatGPT

For image processing, in my examples, I instructed the chat not to use the standard PIL library, but to prefer OpenCV.

#### Image Downsizing

    Create a new image 640 pixels wide without changing the aspect and name it "result_small", 
    use the OpenCV library and do not use the PIL library. Do not add comments or descriptions, 
    just the link to download the final result.

#### Extract from Image

In this case, it's about extracting a strip from a portrait-type image and transforming it into a landscape-type image.

    Create a new 1024 x 800 image by extracting a strip from the center. The base of the original image is the shorter side, 
    so the strip will be parallel to the shorter side of the original. Use the OpenCV library and do not use the PIL library. 
    Do not add comments or descriptions, just the link to download the final result.

## Prompt Function

For description see [Prompt Function](https://www.promptingguide.ai/applications/pf)

I use this technique to provide context to individual chats, making them specific to a certain sector or functionality rather than being generic.

### Image Generator

The generation of images through artificial intelligence is currently very controversial. It is a very useful discipline to support auxiliary 
graphic activities. For instance, when needing to produce an icon for a new application with some meaningful representation, using a traditional 
editor requires hours of work, especially if graphics aren't central to our daily activities. By using a prompt generator and inputting the results 
into an application that produces images from text, we can obtain a dozen professional-level proposals in just a few minutes.

The controversy lies in the fact that designers, who still use their imagination and traditional tools, see their market share being taken away, 
while the customer obtains comparable images at almost no cost. In this scenario, it will be challenging to resist the new trend.

In the realm of art, on the other hand, it's reasonable to ask whether the recombination of styles and ideas done by artificial intelligence 
can be considered an artistic movement. If we accept this premise, we run the risk of flattening our culture, because artificial intelligence 
truly lacks imagination.

See [Image Functions' Section](image/image_functions.md) for some examples.

### Natural Language Translator

One of these sectors is translations into a foreign language. The condition for use is that the user has sufficient knowledge to determine 
if the translation is contextualized and not offensive. The advantage is that one often expands their knowledge of the language in question. 
The source can also be a fairly complex paragraph, but not entire documents.

See [Translator Functions' Section](translator/translator_functions.md) for some examples.

