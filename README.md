Originally forked and inspired by https://github.com/so0k/powerline-kubernetes

# Powerline Kubernetes
A [Powerline](https://github.com/powerline/powerline) segment to show the current Kubernetes context.

## Requirements
PIP packages:  
 - kubectl 
 - [kubernetes Python API](https://pypi.org/project/kubernetes/).

## Installation
Installing the Kubernetes segment can be done with `pip`:

```
$ pwd
/home/user/powerline-kubernetes/

$ pip3 install -e .
```

The Kubernetes segment uses a couple of custom highlight groups. You'll need to define those groups in your colorscheme, for example in `.config/powerline/colorschemes/default.json`:

```json
{
  "groups": {
    "kubernetes_cluster":         { "fg": "gray10", "bg": "darkestblue", "attrs": [] },
    "kubernetes_cluster:alert":   { "fg": "gray10", "bg": "darkestred",  "attrs": [] },
    "kubernetes_namespace":       { "fg": "gray10", "bg": "darkestblue", "attrs": [] },
    "kubernetes_namespace:alert": { "fg": "gray10", "bg": "darkred",     "attrs": [] },
    "kubernetes:divider":         { "fg": "gray4",  "bg": "darkestblue", "attrs": [] }
  }
}
```

Then you can activate the Kubernetes segment by adding it to your segment configuration.
To find powerline configuration refer to https://powerline.readthedocs.io/en/master/configuration.html

Example shell powerline: `.config/powerline/themes/shell/default.json`:

```javascript
{
    "function": "powerline_kubernetes.kubernetes",
    "priority": 30,
    "args": {
        "show_kube_logo": true,
        "show_cluster": true,
        "show_namespace": true,
        "show_default_namespace": false,
        "alerts": [
          "live",
          "cluster:live"
        ]
    }
}
```

By default the segment will look for the Kubernetes config variable `KUBECONFIG`, if not present then the segment will not be displayed.
