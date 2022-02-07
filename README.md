
# Basically deeplinking for instagram and twitter
If your trying to deeplink into an app or something , its easy 
you can play with the code if you like or not 


## Badges



[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Deployment

To deploy this project run

```bash
  pip3 install -r requirements.txt

  also you must have uvicorn 
```


## API Reference

#### Get all items


```http
  GET /instagram/{url_to_your_profile}
```

| Parameter | Type     | 
| :-------- | :------- |
| `id`      | `string` | 




```http
  GET /twitter/{url_to_your_profile}
```

| Parameter | Type     | 
| :-------- | :------- |
| `id`      | `string` | 




## Authors

- [@thewisejun](https://www.github.com/thewisejun)


## Demo

Insert gif or link to demo

https://app.contentmatches.com:8000/instagram/officialcontentmatch
