## Testing the wfc c++ port

In this implementation we use the overlapping model.

Screenshots - 

1)  Lake - ![alt-text](https://github.com/ishaan95/testingwfc/blob/master/testfolder/Lake.png)  


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
