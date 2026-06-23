from pathlib import Path
root = Path(__file__).resolve().parents[1]
def read(rel): return (root/rel).read_text(encoding='utf-8', errors='ignore')
def ok(name, cond):
    if not cond: raise SystemExit(f'FAIL {name}')
    print(f'OK {name}')
required = [
 'SKILL.md','VERSION.md','CHANGELOG.md','README.md','RELEASE_REPORT.md','agents/openai.yaml',
 'handbook/clean-color-note-style.md','handbook/anti-infographic-style.md','handbook/generation-protocol.md','handbook/visual-style.md','handbook/review-rubric.md','tests/test-clean-color-note-style.md',
 'handbook/rendering-engine-routing.md','handbook/content-preprocessing.md','handbook/image-text-boundary.md'
]
for rel in required: ok(f'{rel} exists', (root/rel).exists())
skill = read('SKILL.md')
ok('version v1.4.1', '\u7248\u672c\uff1av1.4.1' in skill and 'Current version: v1.4.1' in read('VERSION.md'))
ok('engine hardwired in skill', '\u51fa\u56fe\u5f15\u64ce\u5199\u6b7b' in skill and '\u9ed8\u8ba4\u4e14\u5f3a\u5236\u4f7f\u7528\u56fe\u7247\u751f\u6210\u6a21\u578b' in skill)
reng = read('handbook/rendering-engine-routing.md')
ok('engine hardwired handbook', '\u5199\u6b7b\u9ed8\u8ba4' in reng and '\u7981\u6b62\u501f\u53e3\u5207\u6362' in reng)
ok('content preprocessing in skill', '\u5185\u5bb9\u524d\u7f6e\u7406\u89e3\u4e0e\u7ed3\u6784\u5316' in skill)
ok('content preprocessing handbook', '\u62bd\u53d6\u6761\u76ee\u5e76\u8ba1\u6570' in read('handbook/content-preprocessing.md'))
ok('title count rule in skill', '\u6807\u9898\u2014\u753b\u9762\u6570\u91cf\u4e00\u81f4\u6027\u6821\u9a8c' in skill)
ok('image text boundary in skill', '\u753b\u9762\u6587\u5b57\u8fb9\u754c' in skill)
ok('image text boundary handbook', '\u9875\u7801\u53ea\u7528\u4e8e\u6587\u4ef6\u540d' in read('handbook/image-text-boundary.md'))
agent = read('agents/openai.yaml')
ok('agent new rules', 'engine_rule' in agent and 'content_rule' in agent and 'title_count_rule' in agent and 'image_text_rule' in agent)
ok('clean color retained', '\u6e05\u723d\u5f69\u8272\u624b\u5199\u7b14\u8bb0' in skill and 'Do not make it monochrome or overly minimal' in skill)
ok('anti infographic retained', '\u53cd\u4fe1\u606f\u56fe\u6f02\u79fb' in read('handbook/anti-infographic-style.md'))
blocked_terms = [chr(23567)+chr(40657), 'Xiao'+'hei', 'xiao'+'hei', 'black '+'creature', 'white-dot '+'eyes', chr(25220)+chr(34989)]
violations=[]
for path in root.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md','.yaml','.yml','.txt'}:
        text=path.read_text(encoding='utf-8', errors='ignore')
        for term in blocked_terms:
            if term in text:
                violations.append(str(path.relative_to(root)))
ok('sensitive reference terms clean', not violations)
print('\nAll v1.4.1 validation checks passed.')
