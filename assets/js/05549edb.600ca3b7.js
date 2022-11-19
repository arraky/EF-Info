"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[674],{5884:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>d,contentTitle:()=>l,default:()=>u,frontMatter:()=>i,metadata:()=>o,toc:()=>p});var r=t(7462),a=(t(7294),t(3905));const i={},l="Numtrip Top Down",o={unversionedId:"numtrip/top-down",id:"numtrip/top-down",title:"Numtrip Top Down",description:"Create Playground",source:"@site/docs/numtrip/top-down.md",sourceDirName:"numtrip",slug:"/numtrip/top-down",permalink:"/EF-Info/docs/numtrip/top-down",draft:!1,editUrl:"https://github.com/arraky/EF-Info/tree/main/docs/numtrip/top-down.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Summary",permalink:"/EF-Info/docs/about-me"}},d={},p=[{value:"Create Playground",id:"create-playground",level:2},{value:"Make Field",id:"make-field",level:3},{value:"Generate Numbers",id:"generate-numbers",level:3},{value:"Playing",id:"playing",level:2},{value:"Ask player to choose a field",id:"ask-player-to-choose-a-field",level:3},{value:"Checking for same numbers",id:"checking-for-same-numbers",level:3},{value:"Marked fields treatment",id:"marked-fields-treatment",level:3}],s={toc:p};function u(e){let{components:n,...t}=e;return(0,a.kt)("wrapper",(0,r.Z)({},s,t,{components:n,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"numtrip-top-down"},"Numtrip Top Down"),(0,a.kt)("h2",{id:"create-playground"},"Create Playground"),(0,a.kt)("h3",{id:"make-field"},"Make Field"),(0,a.kt)("p",null,"Create a pleasing UI with rows, coloumns and a field numbering at the sides"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"def fieldnum():\n    print('  ',end='')\n    for i in range(Row):\n        print('    ',i, end=' ')\n    print('')\n")),(0,a.kt)("p",null,"That's the numbering on top of the field (Coloumns)"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"def line():\n    print('  ', end='')\n    for i in range(Row):\n        print('+------',end='')\n    print('')\n")),(0,a.kt)("p",null,"That's the dividing line between each row"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"def playground():\n    fieldnum()\n    for i in range(Row):\n        line()\n        print(i,end=' ') #*\n        for j in range(Coloumns):\n            if field[i][j] >=10:\n                len = ' '\n            else:\n                len = '  '\n            print(f'|  ',field[i][j], end=len)\n        print('|')\n    line()\n")),(0,a.kt)("p",null,"Integrates the aforehand made definitions "),(0,a.kt)("p",null,"#* integrates row numbering as well"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre"},"playground()\n")),(0,a.kt)("h3",{id:"generate-numbers"},"Generate Numbers"),(0,a.kt)("p",null,"Generate powers of 2 in a field matrix. Starts the game with random numbers"),(0,a.kt)("h2",{id:"playing"},"Playing"),(0,a.kt)("h3",{id:"ask-player-to-choose-a-field"},"Ask player to choose a field"),(0,a.kt)("p",null,'Ask for Row and Coloumn that the chosen field is in, and save it as "The Chosen one" for now'),(0,a.kt)("h3",{id:"checking-for-same-numbers"},"Checking for same numbers"),(0,a.kt)("p",null,'Mark all the directly adjacent fields to "The Chosen one" that happen to have the same number'),(0,a.kt)("h3",{id:"marked-fields-treatment"},"Marked fields treatment"),(0,a.kt)("p",null,"Remove the numbers in the adjacent fields and multiply the Chosen one by 2.\nEmpty fields should be replaced with fields from above"))}u.isMDXComponent=!0}}]);