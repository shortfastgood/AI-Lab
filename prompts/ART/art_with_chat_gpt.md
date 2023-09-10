# ART with ChatGPT

ChatGPT offers a function that uses the ART technique under the name of "advanced data analysis." This function can be activated through the "Settings & Beta"
menu that appears when you click on the three dots at the bottom of the sidebar. Once the option is activated, a new chat of the type "advanced data analysis"
is created. In the prompt line, the + symbol appears, which, when selected, allows you to upload one or more files into the chat.

At this point, it is necessary to formulate a request that leads to the processing of the uploaded data. Once sent, ChatGPT generates an ad-hoc Python program
that is executed. If the outcome is positive, the chat provides a link to download the result; otherwise, it proceeds with error correction. In the end,
it is also possible to download the generated Python code.

The chat has access to the entire standard library of Python. To use ART, there's no need for Python programming knowledge,
but those who have it can influence the chat's decisions.

## Text to PowerPoint presentation

    Please convert the following text into a ten-slide presentation:
    [ This project aims to analyze the advantages and side effects of digital assisted work. 
    Initially, it is a collection of experiences using GitHub's Copilot and OpenAI's ChatGPT. 
    Now, in September 2023, the exploratory phase begins for the use of LLM locally for 
    applications whose data cannot be entrusted to the cloud.]

Replace the text in the quare brakets with your own and execute. The chat will generate a proposal up to ten slides. Then insert:

    Please write the Python code to transform the previous texts into the pptx format.

The chat will generate the python code to generate the presentation. At the end the chat executes the text, after successful execution
the chat shows a link to download the generated pptx file.

    

## Image Processing with ChatGPT

For image processing, in my examples, I instructed the chat not to use the standard PIL library, but to prefer OpenCV.

### Image Downsizing

    Create a new image 640 pixels wide without changing the aspect and name it "result_small", 
    use the OpenCV library and do not use the PIL library. Do not add comments or descriptions, 
    just the link to download the final result.

### Extract from Image

In this case, it's about extracting a strip from a portrait-type image and transforming it into a landscape-type image.

    Create a new 1024 x 800 image by extracting a strip from the center. The base of the original image is the shorter side, 
    so the strip will be parallel to the shorter side of the original. Use the OpenCV library and do not use the PIL library. 
    Do not add comments or descriptions, just the link to download the final result.
