---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.22
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.53
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.23
      win_rate: 0.52
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.5
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.18
      win_rate: 0.44
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.12
      win_rate: 0.69
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.47
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.44
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 1.0
  - name: Captain's Ring
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.5
    - name: Shield
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.3
    win_rate: 0.47
  - name: Bluestone Brooch
    pick_rate: 0.23
    win_rate: 0.63
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-14'
  god_win_rate: 0.528169014084507
  god_matches_won: 75
  god_matches_played: 142
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence, Draconic
    Scale, Spectral Armor, Soul Gem, Leviathan''s Hide, Mantle Of Discord, Stone of
    Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Ancile, Screeching
    Gargoyle, Xibalban Effigy, Void Shield, Gladiator''s Shield, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.12
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.52
      win: 0.53
      pick: 0.25
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.63
    Stampede:
      total: 0.55
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.41
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Freya''s Tears, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s Grace,
    Erosion, Eye of Providence, Phoenix Feather, Spectral Armor, Draconic Scale, Blood-Bound
    Book, Bancroft''s Talon, Lifebinder, Leviathan''s Hide, Midgardian Mail, Glorious
    Pridwen, Helm of Radiance, Yogi''s Necklace, Jade Scepter, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.56
      pick: 0.12
      fit: 0.5
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.91
    Stampede:
      total: 0.55
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Stampede
  flex_slots:
  - Genji's Guard
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita Charm, Freya''s
    Tears, Stone of Binding, Screeching Gargoyle, Spear of the Magus, Void Shield,
    Oni Hunter''s Garb, The Cosmic Horror, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Erosion, Obsidian Shard, Spectral Armor, Eye of Providence, Draconic
    Scale, Helm of Radiance, Leviathan''s Hide, Mantle Of Discord, Midgardian Mail,
    The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.53
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.25
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.56
      pick: 0.12
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.61
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  - Stampede
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Freya''s Tears, Amanita Charm,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion,
    Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic Scale, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Yogi''s Necklace, Mantle Of Discord, Stone
    of Binding, Spear of the Magus, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp,
    Bancroft''s Talon.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.2
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.45
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.35
    Stampede:
      total: 0.52
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.23
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Stampede
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Soul
    Gem, Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire, Oni Hunter''s
    Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation, Chandra''s
    Grace, Erosion, Spectral Armor, Gladiator''s Shield, Eye of Providence, Prophetic
    Cloak, Helm of Radiance, Draconic Scale, Gem of Focus, Leviathan''s Hide, Spear
    of the Magus, Rod of Asclepius, Midgardian Mail, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.45
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.12
      fit: 0.59
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.27
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - The Crusher
  - Stampede
  flex_slots:
  - The Crusher
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Kinetic Cuirass, Freya''s Tears, Amanita Charm, Soul Gem,
    Hydra''s Lament, Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion,
    Spectral Armor, Death Metal, Spear of the Magus, Eye of Providence, Shogun''s
    Ofuda, The Reaper, Draconic Scale, Damaru, The Cosmic Horror, Avenging Blade,
    Helm of Radiance, Riptalon, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Silverbranch Bow, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.47
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Stampede
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Berserker''s
    Shield, Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Freya''s Tears, Amanita
    Charm, Soul Gem, Oni Hunter''s Garb, Spear of the Magus, Hydra''s Lament, Death
    Metal, The Cosmic Horror, Runeforged Hammer, Helm of Radiance, Pharaoh''s Curse,
    Shield of the Phoenix, Shield Splitter, Spectral Armor, Golden Blade, Spear of
    Desolation, Erosion, Rod of Asclepius, Lernaean Bow, Eye of the Storm, Eye of
    Providence, Jade Scepter, Obsidian Shard, Draconic Scale, Bracer of The Abyss,
    Shogun''s Ofuda, Chronos'' Pendant, Leviathan''s Hide, Blood-Bound Book, Bragi''s
    Harp, Riptalon, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.21
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.51
    Stampede:
      total: 0.53
      efficiency: 0.48
      win: 0.69
      pick: 0.19
      fit: 0.25
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Oni Hunter's Garb
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Freya''s Tears, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye of Providence,
    Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Ancile, Screeching
    Gargoyle, Xibalban Effigy, Void Shield, Gladiator''s Shield, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.29
      fit: 0.35
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.66
      win: 0.44
      pick: 0.25
      fit: 0.35
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.12
      fit: 0.57
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.63
  starter: *id001
---
