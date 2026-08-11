---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.48
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.55
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.24
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.63
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.54
  - name: Stampede
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.49
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.05
    win_rate: 0.65
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.12
      win_rate: 0.65
    - name: Draconic Scale
      pick_rate: 0.04
      win_rate: 0.43
  - name: Olmec Blue
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.47
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.69
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.32
    win_rate: 0.55
  - name: Bluestone Brooch
    pick_rate: 0.24
    win_rate: 0.61
  - name: Selflessness
    pick_rate: 0.09
    win_rate: 0.59
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-10'
  god_win_rate: 0.5684754521963824
  god_matches_won: 440
  god_matches_played: 774
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Breastplate of Valor, Oni Hunter''s Garb, Shield of the Phoenix, Erosion, Eye
    of Providence, Spectral Armor, Soul Gem, Leviathan''s Hide, Mantle Of Discord,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Draconic Scale,
    Ancile, Screeching Gargoyle, Xibalban Effigy, Void Shield, Gladiator''s Shield,
    Rod of Asclepius, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.14
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.57
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.32
      fit: 0.63
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s
    Grace, Breastplate of Valor, Erosion, Eye of Providence, Phoenix Feather, Spectral
    Armor, Blood-Bound Book, Bancroft''s Talon, Lifebinder, Leviathan''s Hide, Midgardian
    Mail, Glorious Pridwen, Helm of Radiance, Jade Scepter, Yogi''s Necklace, Ancile,
    Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.5
    Shifter's Shield:
      total: 0.54
      efficiency: 0.52
      win: 0.55
      pick: 0.32
      fit: 0.61
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.91
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem,
    Amanita Charm, Stone of Binding, Breastplate of Valor, Screeching Gargoyle, Spear
    of the Magus, Void Shield, Oni Hunter''s Garb, The Cosmic Horror, Void Stone,
    Shield of the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Obsidian
    Shard, Eye of Providence, Helm of Radiance, Leviathan''s Hide, Mantle Of Discord,
    Midgardian Mail, Doom Orb, Draconic Scale.'
  slot_scores:
    Stone of Binding:
      total: 0.5
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.25
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.41
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.61
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.32
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Breastplate of Valor, Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral
    Armor, Erosion, Bracer of The Abyss, Eye of Providence, Helm of Radiance, Death
    Metal, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord, Yogi''s Necklace,
    Stone of Binding, Spear of the Magus, Bragi''s Harp, Rod of Asclepius, Blood-Bound
    Book, Bancroft''s Talon, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.2
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Kinetic Cuirass, Soul Gem, Amanita Charm, Shield of the Phoenix, Gluttonous Grimoire,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation,
    Chandra''s Grace, Erosion, Spectral Armor, Gladiator''s Shield, Eye of Providence,
    Prophetic Cloak, Helm of Radiance, Gem of Focus, Death Metal, Leviathan''s Hide,
    Rod of Asclepius, Spear of the Magus, Midgardian Mail, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.45
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.66
      win: 0.49
      pick: 0.14
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.59
    Shifter's Shield:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.32
      fit: 0.42
    Soul Gem:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Breastplate
    of Valor, Hydra''s Lament, Soul Gem, Runeforged Hammer, Shield Splitter, Oni Hunter''s
    Garb, Pharaoh''s Curse, Golden Blade, Lernaean Bow, Eye of the Storm, Shield of
    the Phoenix, Death Metal, Erosion, Spectral Armor, Spear of the Magus, Eye of
    Providence, Damaru, The Reaper, Shogun''s Ofuda, Avenging Blade, The Cosmic Horror,
    Helm of Radiance, Leviathan''s Hide, Riptalon, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Tekko-Kagi, Spear of Desolation, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.23
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita
    Charm, Soul Gem, Breastplate of Valor, Oni Hunter''s Garb, Spear of the Magus,
    Death Metal, Hydra''s Lament, Runeforged Hammer, The Cosmic Horror, Helm of Radiance,
    Shield Splitter, Pharaoh''s Curse, Shield of the Phoenix, Golden Blade, Spectral
    Armor, Spear of Desolation, Rod of Asclepius, Lernaean Bow, Erosion, Eye of the
    Storm, Eye of Providence, Jade Scepter, Obsidian Shard, Bracer of The Abyss, Shogun''s
    Ofuda, Chronos'' Pendant, Damaru, Bragi''s Harp, Leviathan''s Hide, Blood-Bound
    Book, The Reaper, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.21
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.51
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.4
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
    Freya''s Tears, Breastplate of Valor, Oni Hunter''s Garb, Shield of the Phoenix,
    Erosion, Eye of Providence, Draconic Scale, Spectral Armor, Soul Gem, Leviathan''s
    Hide, Mantle Of Discord, Stone of Binding, Midgardian Mail, Helm of Radiance,
    Magi''s Cloak, Ancile, Screeching Gargoyle, Xibalban Effigy, Void Shield, Hide
    of the Nemean Lion, Gladiator''s Shield, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.57
      pick: 0.3
      fit: 0.35
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.66
      win: 0.49
      pick: 0.14
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.5
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.65
      pick: 0.11
      fit: 0.57
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
