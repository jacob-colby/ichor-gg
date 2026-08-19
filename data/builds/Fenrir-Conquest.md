---
type: smite-build
god: Fenrir
mode: Conquest
builds:
- source: community
  aspect: Aspect of Loyalty
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.59
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: The Reaper
      pick_rate: 0.18
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.65
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.59
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.14
      win_rate: 0.59
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.78
  - name: Genji's Guard
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.75
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Magi's Cloak
      pick_rate: 0.07
      win_rate: 0.33
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.4
  - name: Heartseeker
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.8
    - name: Magi's Cloak
      pick_rate: 0.05
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.4
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.2
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.23
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.46
  - name: Death's Embrace
    pick_rate: 0.12
    win_rate: 0.61
  source_url: https://smitebrain.com/gods/fenrir/
  last_verified: '2026-08-19'
  god_win_rate: 0.574468085106383
  god_matches_won: 108
  god_matches_played: 188
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Freya's Tears
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Hydra''s Lament, Pendulum Blade, Tekko-Kagi, Runeforged
    Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence,
    Avenging Blade, Dominance, Arondight, Shield Splitter, Eye of the Storm, Tyrfing,
    Riptalon, Silverbranch Bow, Breastplate of Valor, Deathbringer, Barbed Carver,
    Berserker''s Shield, Genji''s Guard, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.31
      fit: 1.0
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.71
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.09
    The Reaper:
      total: 0.6
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.91
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.62
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 1.0
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Freya''s
    Tears, The Crusher, Hydra''s Lament, Breastplate of Valor, Genji''s Guard, Runeforged
    Hammer, Damaru, Transcendence, Dominance, Pendulum Blade, Lernaean Bow, Arondight,
    Oni Hunter''s Garb, Berserker''s Shield, Golden Blade, Tekko-Kagi, Avenging Blade,
    Kinetic Cuirass, Shield Splitter, Amanita Charm, Shield of the Phoenix, Eye of
    the Storm, Tyrfing, Eye of Providence, Yogi''s Necklace, Riptalon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.5
      pick: 0.31
      fit: 0.71
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.14
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.57
    Titan's Bane:
      total: 0.56
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Freya''s Tears, The Crusher, Hydra''s Lament, Pendulum Blade, Breastplate
    of Valor, Genji''s Guard, Runeforged Hammer, Tekko-Kagi, Riptalon, Arondight,
    Damaru, Silverbranch Bow, Shield of the Phoenix, Berserker''s Shield, Lernaean
    Bow, Kinetic Cuirass, Amanita Charm, Screeching Gargoyle, Golden Blade, Chandra''s
    Grace, Eye of Providence, Transcendence, Avenging Blade, Oni Hunter''s Garb, Dominance,
    Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.64
      win: 0.5
      pick: 0.31
      fit: 0.78
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.22
    The Reaper:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.56
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.66
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Freya's Tears
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    The Crusher, Berserker''s Shield, Yogi''s Necklace, Runeforged Hammer, Oni Hunter''s
    Garb, Eye of the Storm, Chandra''s Grace, Erosion, Shield Splitter, Phoenix Feather,
    Eye of Providence, Spectral Armor, Draconic Scale, Riptalon, Breastplate of Valor,
    Golden Blade, Hydra''s Lament, Pharaoh''s Curse, Avenging Blade, Leviathan''s
    Hide, Genji''s Guard, Midgardian Mail, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.54
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.38
    The Reaper:
      total: 0.57
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.7
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.5
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 0.5
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Freya's Tears
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Freya's Tears
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Tekko-Kagi, Pendulum Blade, Riptalon, Avenging Blade,
    Silverbranch Bow, Avatar''s Parashu, Hydra''s Lament, Runeforged Hammer, Damaru,
    Toxic Blade, Lernaean Bow, Screeching Gargoyle, Golden Blade, Transcendence, Breastplate
    of Valor, Berserker''s Shield, Dominance, Shield Splitter, Eye of the Storm, Stone
    of Binding, Tyrfing, Oath-Sworn Spear, Genji''s Guard, Arondight, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.31
      fit: 1.0
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.06
    The Reaper:
      total: 0.61
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.94
    Tekko-Kagi:
      total: 0.54
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 1.0
    Titan's Bane:
      total: 0.62
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Freya's Tears
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Golden Blade
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Riptalon, The Crusher, Golden Blade, Silverbranch Bow,
    Tyrfing, Berserker''s Shield, Lernaean Bow, Toxic Blade, Dominance, Tekko-Kagi,
    Hydra''s Lament, Pharaoh''s Curse, Qin''s Blade, Runeforged Hammer, Breastplate
    of Valor, Damaru, Shogun''s Ofuda, Kinetic Cuirass, Genji''s Guard, Amanita Charm,
    Eye of Providence, Oni Hunter''s Garb, Eros'' Bow, Transcendence, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.69
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.04
    Riptalon:
      total: 0.55
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.79
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.43
    Titan's Bane:
      total: 0.53
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Hydra''s Lament, Breastplate
    of Valor, The Crusher, Genji''s Guard, Shield of the Phoenix, Pendulum Blade,
    Arondight, Screeching Gargoyle, Chandra''s Grace, Gladiator''s Shield, Runeforged
    Hammer, Berserker''s Shield, Prophetic Cloak, Kinetic Cuirass, Damaru, Amanita
    Charm, Riptalon, Eye of Providence, Oni Hunter''s Garb, Regrowth Striders, Lernaean
    Bow, Silverbranch Bow, Golden Blade, Tekko-Kagi, Transcendence.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.5
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.5
      pick: 0.31
      fit: 0.85
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.75
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.75
      pick: 0.12
      fit: 0.5
    The Crusher:
      total: 0.54
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 0.45
    Titan's Bane:
      total: 0.54
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Hydra''s Lament, Pendulum Blade, Tekko-Kagi,
    Runeforged Hammer, Damaru, Lernaean Bow, Avatar''s Parashu, Golden Blade, Transcendence,
    Avenging Blade, Dominance, Arondight, Shield Splitter, Genji''s Guard, Eye of
    the Storm, Tyrfing, Riptalon, Silverbranch Bow, Breastplate of Valor, Deathbringer,
    Barbed Carver, Berserker''s Shield, Musashi''s Dual Swords, Bloodforge.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.64
      win: 0.5
      pick: 0.31
      fit: 1.0
    Hydra's Lament:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.71
    The Reaper:
      total: 0.6
      efficiency: 0.52
      win: 0.61
      pick: 0.18
      fit: 0.91
    The Crusher:
      total: 0.62
      efficiency: 0.64
      win: 0.54
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.53
      efficiency: 0.41
      win: 0.5
      pick: 0.17
      fit: 1.0
    Titan's Bane:
      total: 0.62
      efficiency: 0.45
      win: 0.67
      pick: 0.25
      fit: 1.0
  starter: *id001
---
