# poya

Tells you when the next poya day is. https://nextpoyawhen.com

## Poya?

Poya occurs every full moon day. It's a public holiday in Sri Lanka, so everyone here loves when it's Poya.

## API

You can get the JSON array of poya days from the endpoint https://nextpoyawhen.com/poya.json

## Development

After making changes to `index.html`, run `./replace.sh` to update the poya days array. It will overwrite the `index-stage.html` file. This latter HTML fie is what you should run in the browser.

To automatically replace when `index.html` is updated, use a command like `fswatch`:

```bash
fswatch index.html | xargs -n1 -I{} ./replace.sh
```

To deploy the changes to S3, run `./deploy`.
