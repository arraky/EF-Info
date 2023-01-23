"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[348],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>h});var a=n(7294);function l(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){l(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function r(e,t){if(null==e)return{};var n,a,l=function(e,t){if(null==e)return{};var n,a,l={},o=Object.keys(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||(l[n]=e[n]);return l}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)n=o[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(l[n]=e[n])}return l}var s=a.createContext({}),d=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},u=function(e){var t=d(e.components);return a.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},c=a.forwardRef((function(e,t){var n=e.components,l=e.mdxType,o=e.originalType,s=e.parentName,u=r(e,["components","mdxType","originalType","parentName"]),c=d(n),h=l,f=c["".concat(s,".").concat(h)]||c[h]||p[h]||o;return n?a.createElement(f,i(i({ref:t},u),{},{components:n})):a.createElement(f,i({ref:t},u))}));function h(e,t){var n=arguments,l=t&&t.mdxType;if("string"==typeof e||l){var o=n.length,i=new Array(o);i[0]=c;var r={};for(var s in t)hasOwnProperty.call(t,s)&&(r[s]=t[s]);r.originalType=e,r.mdxType="string"==typeof e?e:l,i[1]=r;for(var d=2;d<o;d++)i[d]=n[d];return a.createElement.apply(null,i)}return a.createElement.apply(null,n)}c.displayName="MDXCreateElement"},4685:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>p,frontMatter:()=>o,metadata:()=>r,toc:()=>d});var a=n(7462),l=(n(7294),n(3905));const o={},i="Working game?",r={permalink:"/EF-Info/2022/12/31/numtrip-update",editUrl:"https://github.com/arraky/EF-Info/tree/main/blog/2022-12-31-numtrip-update.md",source:"@site/blog/2022-12-31-numtrip-update.md",title:"Working game?",description:"Inputchecks",date:"2022-12-31T00:00:00.000Z",formattedDate:"31. Dezember 2022",tags:[],readingTime:4.3,hasTruncateMarker:!1,authors:[],frontMatter:{},prevItem:{title:"What was it all for?",permalink:"/EF-Info/2023/1/13/numtrip-conclusion"},nextItem:{title:"Recursion",permalink:"/EF-Info/2022/12/6/numtrip-update"}},s={authorsImageUrls:[]},d=[{value:"Inputchecks",id:"inputchecks",level:2},{value:"Chechadj()",id:"chechadj",level:2},{value:"Replacetop()",id:"replacetop",level:2},{value:"Giveup()",id:"giveup",level:2},{value:"Endgameloss()",id:"endgameloss",level:2},{value:"Endgamewin()",id:"endgamewin",level:2},{value:"Gameloop:",id:"gameloop",level:2},{value:"Game with variable field sizes",id:"game-with-variable-field-sizes",level:2}],u={toc:d};function p(e){let{components:t,...n}=e;return(0,l.kt)("wrapper",(0,a.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,l.kt)("h2",{id:"inputchecks"},"Inputchecks"),(0,l.kt)("p",null,"I removed the is_integer function and replaced it with a function in the X and Y Inputcheck:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"    inpx = \"\".join(filter(lambda x: x in ['0','1','2','3','4','5','6','7','8','9','-'],input(Questionx))) \n")),(0,l.kt)("p",null,"Lambda defines a function here: Filter out everything that's not in '0123456789-'"),(0,l.kt)("p",null,"It then goes on about and checks if the if the len(inpx) is 1.\nIf that's not the case, it tells you to f*ck off."),(0,l.kt)("p",null,"jk "),(0,l.kt)("p",null,"It just tells you the input was invalid and the whole process starts anew."),(0,l.kt)("h2",{id:"chechadj"},"Chechadj()"),(0,l.kt)("p",null,'It has a global adjacent list "adjlist". TBH I took this idea from Thomas (props to him). '),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("p",{parentName:"li"},'The function now has 4 parameters instead of 2: x,y,oldx and oldy. Again, too fix "referenced before assignment errors"')),(0,l.kt)("li",{parentName:"ul"},(0,l.kt)("p",{parentName:"li"},"Instead of not_left, not_right etc. the functions now check if there is something instead of nothing -> "))),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"        left = (x > 0 and field[y][x] == field[y][x - 1] and field[y][x]!=0) or False\n")),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"Now, most importantly, I got the recursion to work: E.g. If left, it appends this field to the adjlist, sets the current field to 0 and repeats the function on the square to the left")),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"        if left:\n            adjlist.append([y,x-1])\n            field[y][x] = 0\n            checkadj(x-1,y,oldy,oldx)\n")),(0,l.kt)("h2",{id:"replacetop"},"Replacetop()"),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"It takes the adjlist and sorts it at the beginning, so that it works from the top of the field downwards. This fixes some errors."),(0,l.kt)("li",{parentName:"ul"},"I gave each element in the adjlist a name in a for loop:")),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"        for i in range(len(adjlist)):\n        dy = adjlist[i][0]\n        dx = adjlist[i][1]\n")),(0,l.kt)("ul",null,(0,l.kt)("li",{parentName:"ul"},"The function takes the number from the field from above and puts it into field","[dy][dx]"," and replaces this top field with 0. Dy is subtracted by 1 and the process begins again for the field that currently has a 0 in it. The moment it reaches the top, it gives this square a new number:")),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"        while dy != 0:\n            field[dy][dx] = field[dy-1][dx]\n            field[dy-1][dx] = 0\n            dy-=1\n        field[0][dx] = 2**(randint(0,3))\n")),(0,l.kt)("h2",{id:"giveup"},"Giveup()"),(0,l.kt)("p",null,"I provisorically created this function as a jump in for the lack of a working endgame() function. I may change it to a stop game function that saves the current playfield via JSON to another file. "),(0,l.kt)("h2",{id:"endgameloss"},"Endgameloss()"),(0,l.kt)("p",null,'This function checks on the whole field, if there\'s even a possible merge of fields. For this, I chose my function chechadj(x,y,oldx,oldy). To make it work, I had to create a new list "endgameplayfield", which copies the whole content of the playfield'),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"    global field\n    endgameplayfield = [x[:] for x in field]\n")),(0,l.kt)("p",null,"Now in two for loops, it checks if Checkadj() is true. In checkadj() fields change their values though, so in the end, it copies those values back from the endgameplayfield"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"    for i in range(5):\n        for j in range(5):\n            if checkadj(j,i, oldx=j, oldy=i) is True:\n                field = [x[:] for x in endgameplayfield]\n                adjlist.clear()\n                return False #Continue game\n")),(0,l.kt)("p",null,"The return False tells my gameloop to continue. If there's no field to merge, you lost and it stops the loop and gives the player a game over message:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"    print(f'Alas, you lost! You lasted {roundcount} rounds')\n    return True #Loss\n")),(0,l.kt)("p",null,"The roundcount is in the gameloop"),(0,l.kt)("h2",{id:"endgamewin"},"Endgamewin()"),(0,l.kt)("p",null,"This function takes every value in the field and looks for the winning number, I set it to 256 for now. "),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"    for i in range(5):\n        for j in range(5):\n            if field[i][j] == 256:\n                return True#Win\n")),(0,l.kt)("h2",{id:"gameloop"},"Gameloop:"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-py"},"    while endgameloss() is False:\n    if roundcount == 0: #show it the first time\n        playground()\n    else:\n        pass\n\n    x = X_Inputcheck('X Axis:') #Inputs\n    y = Y_Inputcheck('Y Axis:')\n\n    oldy,oldx = y,x #Stores values for later\n    oldfield = field[y][x]\n\n    print(f'You chose the field with the number:', field[y][x]) #Inform the player that the right field was chosen\n\n    checkdel_and_double() #Recursion delete\n    replacetop() #Fill up\n\n    adjlist.clear() #Clear list, so it doesn't annoy us in the next round\n    if endgamewin() is True: #Check if win condition is met; if so -> Congratulations\n        print(f'You won! It took you {roundcount} rounds')\n        break\n    roundcount+=1 #counts the rounds\n    print('New Field:')\n    playground() #show the end result so that you can play again\n")),(0,l.kt)("p",null,"I wrote the most important infos in it already. "),(0,l.kt)("ol",null,(0,l.kt)("li",{parentName:"ol"},"It starts by showing the player the playground in round 0. "),(0,l.kt)("li",{parentName:"ol"},"Asks for inputs and stores those values for later."),(0,l.kt)("li",{parentName:"ol"},"I added a small print that shows the player the number in the field he chose."),(0,l.kt)("li",{parentName:"ol"},"Goes through the recursion and filling up functions"),(0,l.kt)("li",{parentName:"ol"},"Clears the adjlist for the next roudn"),(0,l.kt)("li",{parentName:"ol"},"Checks if you've won and shows the amount of rounds it took you"),(0,l.kt)("li",{parentName:"ol"},"Adds 1 to the roundcount and shows the new field")),(0,l.kt)("h2",{id:"game-with-variable-field-sizes"},"Game with variable field sizes"),(0,l.kt)("p",null,'It\'s basically the same thing, I just replaced the hard written code (values like 4 and 5) with variables "Col" and "Row". At the beginning of the game, the player is asked for the size of the field. The input is checked through the same functions as X and Y_Inputcheck.'),(0,l.kt)("p",null,"I must rewrite it though, as it currently allows for 1x1 fields which obviously don't work. And even other fields such as 1x5 tend to have no solution as it's all based on random (pseudorandom to be exact) numbers."))}p.isMDXComponent=!0}}]);