---
layout: dir
title: ptkyr/notes
cmd: ls -la
pwd: notes
---

{% assign subjs = "jp, pmath, cs, co" | split: "," %}

{% for subject in subjs %}
<span class="prompt host"><a href = "/">ptkyr</a></span>
<span class="prompt path">
        <a href = "/">~</a><a href = "/{{page.pwd}}" class="dir">{{page.pwd}}</a>
</span>
<span class="prompt cmd">ls</span> -la {{subject}}
<nav class="term">
    total {{ site.notes.subject.size | plus: 2 }}
</nav>
<table class="term">
    <nav class="term">
        <tr class = "mobile-hidden">
            <td class = "term ls-la">drwxr-xr-x</td>
            <td class = "term ls-la num">32</td>
            <td class = "term ls-la author">ptkyr</td>
            <td class = "term ls-la">users</td>
            <td class = "term ls-la size">64</td>
            <td class = "term ls-la date">{{ site.time | date: "%b" }}&nbsp;{{ site.time | date: "%_e%t%Y" }}</td>
            <td class = "term ls-la"><a class="term-nav file" href="">.</a></td>
        </tr>
    </nav>
    <nav class="term">
        <tr class = "mobile-hidden">
            <td class = "term ls-la">drwxr-xr-x</td>
            <td class = "term ls-la num">32</td>
            <td class = "term ls-la author">ptkyr</td>
            <td class = "term ls-la">users</td>
            <td class = "term ls-la size">64</td>
            <td class = "term ls-la date">{{ site.time | date: "%b" }}&nbsp;{{ site.time | date: "%_e%t%Y" }}</td>
            <td class = "term ls-la"><a class="term-nav file" href="/index.html">..</a></td>
        </tr>
    </nav>
     {% for item in site.notes %}
     echo item.title
        <nav class="term">
        <tr>
            <td class = "term ls-la mobile-hidden">-rw-r--r--</td>
            <td class = "term ls-la mobile-hidden num">1</td>
            <td class = "term ls-la mobile-hidden author">{{ item.author | split: " " | first | downcase }}</td>
            <td class = "term ls-la mobile-hidden">users</td>
            <td class = "term ls-la mobile-hidden size">{{ item.content | size }}</td>
            <td class = "term ls-la date">{{ item.date | date: "%b" }}&nbsp;{{ item.date | date: "%_e%t%Y" }}</td>
            <td><a class="term-nav file" href="{{ item.url }}">{{ item.title }}</a></td>
        </tr>
        </nav>
    {% endfor %}
</table>
{% endfor %}


<nav class="term">
    total {{ site.data.notes.size | plus: 2 }}
</nav>
<table class="term">
    <nav class="term">
        <tr class = "mobile-hidden">
            <td class = "term ls-la">drwxr-xr-x</td>
            <td class = "term ls-la num">32</td>
            <td class = "term ls-la author">ptkyr</td>
            <td class = "term ls-la">users</td>
            <td class = "term ls-la size">64</td>
            <td class = "term ls-la date">{{ site.time | date: "%b" }}&nbsp;{{ site.time | date: "%_e%t%Y" }}</td>
            <td class = "term ls-la"><a class="term-nav file" href="">.</a></td>
        </tr>
    </nav>
    <nav class="term">
        <tr class = "mobile-hidden">
            <td class = "term ls-la">drwxr-xr-x</td>
            <td class = "term ls-la num">32</td>
            <td class = "term ls-la author">ptkyr</td>
            <td class = "term ls-la">users</td>
            <td class = "term ls-la size">64</td>
            <td class = "term ls-la date">{{ site.time | date: "%b" }}&nbsp;{{ site.time | date: "%_e%t%Y" }}</td>
            <td class = "term ls-la"><a class="term-nav file" href="/index.html">..</a></td>
        </tr>
    </nav>

    {% for item in site.notes %}
        {% if item.symlink %}
            <tr>
                <td class = "term ls-la mobile-hidden">lrwxrwxrwx</td>
                <td class = "term ls-la mobile-hidden num">1</td>
                <td class = "term ls-la mobile-hidden author">ptkyr</td>
                <td class = "term ls-la mobile-hidden">users</td>
                <td class = "term ls-la mobile-hidden size">32</td>
                <td class = "term ls-la date">{{ item.date | date: "%b" }}&nbsp;{{ item.date | date: "%_e%t%Y" }}</td>
                <td><a class="term-nav symlink" href="{{ item.symlink }}">{{ item.title }}.{{ item.extension | default: "mp4" }}</a></td>
            </tr>
        {% else if item.pdf %}
            <nav class="term">
            <tr>
                <td class = "term ls-la mobile-hidden">-rw-r--r--</td>
                <td class = "term ls-la mobile-hidden num">1</td>
                <td class = "term ls-la mobile-hidden author">ptkyr</td>
                <td class = "term ls-la mobile-hidden">users</td>
                <td class = "term ls-la mobile-hidden size">{{ item.size }}</td>
                <td class = "term ls-la date {% if item.pdf %}mobile-blank{% endif %}">
                    {{ item.date | date: "%b" }}&nbsp;{{ item.date | date: "%_e%t%Y" }}
                </td>
                <td><a class="term-nav file" href="{{ item.pdf }}">{{ item.title }}.pdf</a></td>
            </tr>
            </nav>
        {% else %}
            <nav class="term">
            <tr>
                <td class = "term ls-la mobile-hidden">-rw-r--r--</td>
                <td class = "term ls-la mobile-hidden num">1</td>
                <td class = "term ls-la mobile-hidden author">{{ item.author | split: " " | first | downcase }}</td>
                <td class = "term ls-la mobile-hidden">users</td>
                <td class = "term ls-la mobile-hidden size">{{ item.content | size }}</td>
                <td class = "term ls-la date">{{ item.date | date: "%b" }}&nbsp;{{ item.date | date: "%_e%t%Y" }}</td>
                <td><a class="term-nav file" href="{{ item.url }}">{{ item.title }}</a></td>
            </tr>
            </nav>
        {% endif %}
    {% endfor %}
</table>
