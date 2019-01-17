## Testing the wfc c++ port - originally by Mathieu Fehr and Nathanaël Courant

In this implementation we use the overlapping model.

Screenshots - 

1)     Tile - Lake - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testfolder/Lake.png) . 
       Output - (a) - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/Lake0.png) . 
       Output - (b) - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/Lake1.png) . 
2)     Tile - Magic Office - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testfolder/Magic%20Office.png) . 
       ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/Magic%20Office0.png) . 
       ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/Magic%20Office1.png) . 
3)     Tile - Map - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testfolder/map02_04.png) . 
       ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/map02_040.png) . 
       ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/map02_041.png) . 
4)     Tile - Zelda - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testfolder/zelda.png) . 
       ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/zelda0.png) .  
       ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testresults/zelda1.png) .  


## fast-wfc

An implementation of [Wave Function Collapse](https://github.com/mxgmn/WaveFunctionCollapse) with a focus on performance.
At the time of writing, only the overlapping method has been implemented.

## Requirements

You need a C++-17 compatible compiler.

## Getting started

```
git clone https://github.com/ishaan95/testingwfc && cd testingwfc/
make all
./wfc
```

## Performance

If fast-wfc is an order of magnitude faster than the original WFC algorithm, it is thanks to three main optimizations that have been made to the original algorithm, described below. 

## Third-parties library

The files in `src/lib/` come from:
* RapidXML [https://github.com/dwd/rapidxml](https://github.com/dwd/rapidxml)
* stb Library [https://github.com/nothings/stb](https://github.com/nothings/stb)

## Image samples

The image samples come from [https://github.com/mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)
