# Second Insight
Second Insight revolutionizes investment risk assessment by offering users a comprehensive report, effortlessly navigating the skies of investment risks. Let AI handle the quantitative analysis while humans trust their intuition to make informed investment decisions.

[IvyHacks](https://www.ivyhacks.ai/) - Columbia x Cornell x NYU AI Hackathon

By Homer Quan, Ayan Das, Garv Sehgal, Daniel Chen

## Important Links

[Devpost](https://devpost.com/software/secondinsight)  

[Slides]() {insert slides link}  

[Demo]() {insert youtube link}

## Technology Stack
### Frontend
- Next.js
- Vercel
- Shadcn

### Backend
- FastAPI
- OpenAI
- LlamaIndex
- Polygon.io
- Pandas
- NumPy

## Architecture

<img src="https://github.com/homerlab/ivyhack-risk-advisor/assets/113078548/1e38c6da-38ef-4cc1-91da-1fedf74a9bea" width="800" />

## How to run

* How to run:

1. set openai api key in your enviroment: 
`export OPENAI_API_KEY= xxxxxxx`
2. install node dependences on all four folders in cli_run_model folder 
`npm i .`
3. start model web service: `cd cli_run_model/combined_service; node web.js`
4. start ui web service: `cd cli_run_model/ui; php -S 0.0.0.0:8000`
5. Open "http://local:8000" on you browser

<img width="800" alt="Demo" src="https://github.com/homerlab/ivyhack-risk-advisor/assets/113078548/a0336879-5275-4f33-8207-774c5fbdf3d0">

