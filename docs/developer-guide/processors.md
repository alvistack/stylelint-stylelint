# Writing processors

Processors are functions that hook into Stylelint's pipeline, modifying code on its way into Stylelint and modifying results on their way out.

**Their use is discouraged in favor of [custom syntaxes](syntaxes.md).**

Processor modules are functions that accept an options object and return an object with the following the functions, which hook into the processing of each file:

- **code**: A function that accepts two arguments, the file's code and the file's path, and returns a string for Stylelint to lint.
- **result**: A function that accepts two arguments, the file's Stylelint result object and the file's path, and either mutates the result object (returning nothing) or returns a new one.

```js
// my-processor.js
module.exports = function myProcessor(options) {
  return {
    code: (input, filepath) => {
      // ...
      return transformedCode;
    },
    result: (stylelintResult, filepath) => {
      // ...
      return transformedResult;
    }
  };
};
```

_Processor options must be JSON-friendly_ because users will need to include them in `.stylelintrc` files.
