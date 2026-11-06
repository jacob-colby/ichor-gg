---
type: smite-build
god: Jing Wei
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.9
    win_rate: 0.43
    alternates:
    - name: Rage
      pick_rate: 0.03
      win_rate: 0.5
    - name: Tyrfing
      pick_rate: 0.03
      win_rate: 0.5
  - name: Dagger of Frenzy
    pick_rate: 0.84
    win_rate: 0.44
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.04
      win_rate: 0.33
    - name: Rage
      pick_rate: 0.01
      win_rate: 1.0
  - name: Dominance
    pick_rate: 0.39
    win_rate: 0.31
    alternates:
    - name: The Executioner
      pick_rate: 0.33
      win_rate: 0.5
    - name: Riptalon
      pick_rate: 0.06
      win_rate: 0.5
  - name: Silverbranch Bow
    pick_rate: 0.28
    win_rate: 0.5
    alternates:
    - name: Deathbringer
      pick_rate: 0.22
      win_rate: 0.43
    - name: Dominance
      pick_rate: 0.11
      win_rate: 0.29
  - name: Deathbringer
    pick_rate: 0.34
    win_rate: 0.48
    alternates:
    - name: Riptalon
      pick_rate: 0.26
      win_rate: 0.44
    - name: Musashi's Dual Swords
      pick_rate: 0.07
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.1
    win_rate: 0.6
    alternates:
    - name: Deathbringer
      pick_rate: 0.14
      win_rate: 0.29
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.6
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.76
    win_rate: 0.48
  - name: Gilded Arrow
    pick_rate: 0.21
    win_rate: 0.21
  - name: Death's Embrace
    pick_rate: 0.01
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/jing-wei/
  last_verified: '2026-11-06'
  god_win_rate: 0.4264705882352941
  god_matches_won: 29
  god_matches_played: 68
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Demon Blade
  - Deathbringer
  - Riptalon
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Lernaean Bow, Demon Blade, Golden Blade, Rage, Qin''s Blade,
    Tekko-Kagi, The Reaper, Hydra''s Lament, Bloodforge, Barbed Carver, Transcendence,
    Runeforged Hammer, Odysseus'' Bow, Jotunn''s Revenge, Sun Beam Bow, The Crusher,
    Shield Splitter, Eye of the Storm, Avenging Blade, Toxic Blade, Heartseeker, Berserker''s
    Shield.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.75
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.87
    Deathbringer:
      total: 0.49
      efficiency: 0.44
      win: 0.48
      pick: 0.74
      fit: 0.54
    Riptalon:
      total: 0.5
      efficiency: 0.36
      win: 0.6
      pick: 0.31
      fit: 0.57
  community_ordered:
  - Tyrfing
  - Deathbringer
  - Riptalon
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - Silverbranch Bow
  - Riptalon
  flex_slots:
  - Silverbranch Bow
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Tyrfing, Hydra''s Lament, The Reaper, Heartseeker, Tekko-Kagi, The Crusher,
    Lernaean Bow, Titan''s Bane, Arondight, Golden Blade, Rage, Transcendence, Avatar''s
    Parashu, Demon Blade, Toxic Blade, Genji''s Guard, Qin''s Blade, Runeforged Hammer,
    Bloodforge, Barbed Carver, Pendulum Blade, Damaru, Shield Splitter, Eye of the
    Storm, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Transcendence:
      total: 0.43
      efficiency: 0.5
      win: 0.5
      pick: 0.0
      fit: 0.24
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.49
    Hydra's Lament:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.42
    Silverbranch Bow:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.47
      fit: 0.33
    Riptalon:
      total: 0.5
      efficiency: 0.45
      win: 0.6
      pick: 0.31
      fit: 0.39
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Lernaean Bow
  - Rage
  - Tyrfing
  - Demon Blade
  - Deathbringer
  - Riptalon
  flex_slots:
  - Lernaean Bow
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Demon Blade, Lernaean Bow, Rage, Golden Blade, Qin''s Blade,
    The Reaper, Hydra''s Lament, Tekko-Kagi, Bloodforge, Barbed Carver, Transcendence,
    Runeforged Hammer, Jotunn''s Revenge, The Crusher, Odysseus'' Bow, Shield Splitter,
    Eye of the Storm, Sun Beam Bow, Avenging Blade, Heartseeker, Arondight, Berserker''s
    Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Rage:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.03
      fit: 0.57
    Tyrfing:
      total: 0.52
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.71
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.49
      efficiency: 0.44
      win: 0.48
      pick: 0.74
      fit: 0.57
    Riptalon:
      total: 0.49
      efficiency: 0.36
      win: 0.6
      pick: 0.31
      fit: 0.53
  community_ordered:
  - Rage
  - Tyrfing
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Kinetic Cuirass
  - Shield Splitter
  - Tyrfing
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Phoenix Feather,
    Yogi''s Necklace, Tyrfing, Golden Blade, Shield Splitter, Berserker''s Shield,
    Oni Hunter''s Garb, Runeforged Hammer, Draconic Scale, The Reaper, Shogun''s Ofuda,
    Pharaoh''s Curse, Erosion, Genji''s Guard, Eye of Providence, Bloodforge, Midgardian
    Mail, Shifter''s Shield, Leviathan''s Hide, Lernaean Bow, Hide of the Nemean Lion,
    Stone of Binding, Ancile, Umbral Link, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shield Splitter:
      total: 0.48
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.37
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.49
    Riptalon:
      total: 0.51
      efficiency: 0.36
      win: 0.6
      pick: 0.31
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Tyrfing
  - Riptalon
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Tyrfing
  - Tekko-Kagi
  - Silverbranch Bow
  - The Crusher
  - Riptalon
  - Heartseeker
  flex_slots:
  - The Crusher
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Reaper, Tekko-Kagi, Tyrfing, The Crusher, Heartseeker, Titan''s
    Bane, Jotunn''s Revenge, Toxic Blade, Lernaean Bow, Avatar''s Parashu, Avenging
    Blade, Golden Blade, Rage, Demon Blade, Qin''s Blade, Hydra''s Lament, Oath-Sworn
    Spear, Transcendence, Bloodforge, Runeforged Hammer, Barbed Carver, Pendulum Blade,
    Berserker''s Shield.'
  slot_scores:
    Tyrfing:
      total: 0.49
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.53
    Tekko-Kagi:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.69
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.5
      pick: 0.47
      fit: 0.63
    The Crusher:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.57
    Riptalon:
      total: 0.55
      efficiency: 0.45
      win: 0.6
      pick: 0.31
      fit: 0.72
    Heartseeker:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  - Riptalon
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Dagger of Frenzy
  - Tyrfing
  - Deathbringer
  - Riptalon
  flex_slots:
  - Dagger of Frenzy
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Tyrfing, Golden Blade, Lernaean Bow, Qin''s Blade, Demon Blade, Rage,
    Hydra''s Lament, Tekko-Kagi, The Reaper, Sun Beam Bow, Bloodforge, Transcendence,
    Barbed Carver, Toxic Blade, Runeforged Hammer, Odysseus'' Bow, Jotunn''s Revenge,
    The Crusher, Shield Splitter, Eye of the Storm, Avenging Blade, Heartseeker, Vital
    Amplifier, Berserker''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.55
    Dagger of Frenzy:
      total: 0.47
      efficiency: 0.42
      win: 0.44
      pick: 1.0
      fit: 0.49
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.75
    Deathbringer:
      total: 0.47
      efficiency: 0.44
      win: 0.48
      pick: 0.74
      fit: 0.41
    Riptalon:
      total: 0.5
      efficiency: 0.36
      win: 0.6
      pick: 0.31
      fit: 0.59
  community_ordered:
  - Dagger of Frenzy
  - Tyrfing
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Arondight
  - Deathbringer
  - Riptalon
  flex_slots:
  - Riptalon
  - Deathbringer
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Tyrfing, Arondight, Lernaean Bow, Damaru, Genji''s Guard, Golden Blade, Qin''s
    Blade, Rage, Breastplate of Valor, Demon Blade, Chandra''s Grace, The Reaper,
    Transcendence, Runeforged Hammer, Bloodforge, Tekko-Kagi, Barbed Carver, Screeching
    Gargoyle, Freya''s Tears, Odysseus'' Bow, The Crusher, Eye of Erebus, Berserker''s
    Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.41
    Tyrfing:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.47
    Hydra's Lament:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
    Arondight:
      total: 0.47
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.41
    Deathbringer:
      total: 0.45
      efficiency: 0.44
      win: 0.48
      pick: 0.74
      fit: 0.3
    Riptalon:
      total: 0.46
      efficiency: 0.36
      win: 0.6
      pick: 0.31
      fit: 0.35
  community_ordered:
  - Tyrfing
  - Deathbringer
  - Riptalon
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Rage
  - Dominance
  - Tyrfing
  - Demon Blade
  flex_slots:
  - Golden Blade
  - Rage
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Tyrfing, Lernaean Bow, Demon Blade, Golden Blade, Rage,
    Qin''s Blade, Tekko-Kagi, The Reaper, Hydra''s Lament, Berserker''s Shield, Bloodforge,
    Barbed Carver, Transcendence, Runeforged Hammer, Odysseus'' Bow, Jotunn''s Revenge,
    Sun Beam Bow, The Crusher, Shield Splitter, Eye of the Storm, Avenging Blade,
    Toxic Blade, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.49
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.64
    Rage:
      total: 0.47
      efficiency: 0.46
      win: 0.5
      pick: 0.03
      fit: 0.54
    Dominance:
      total: 0.43
      efficiency: 0.47
      win: 0.31
      pick: 0.61
      fit: 0.64
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.5
      pick: 0.03
      fit: 0.75
    Demon Blade:
      total: 0.48
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.87
  community_ordered:
  - Rage
  - Dominance
  - Tyrfing
  starter: *id001
---
