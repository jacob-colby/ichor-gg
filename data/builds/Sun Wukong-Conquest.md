---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.37
    win_rate: 0.55
    alternates:
    - name: Mystical Mail
      pick_rate: 0.08
      win_rate: 0.62
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.56
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.49
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.6
  - name: Gladiator's Shield
    pick_rate: 0.1
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.2
      win_rate: 0.63
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.62
  - name: Sundering Echo
    pick_rate: 0.14
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.49
    - name: Rod of Tahuti
      pick_rate: 0.1
      win_rate: 0.58
  - name: Draconic Scale
    pick_rate: 0.1
    win_rate: 0.61
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.53
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.44
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.58
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.45
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.29
    win_rate: 0.51
  - name: Archmage's Gem
    pick_rate: 0.09
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-07'
  god_win_rate: 0.5593952483801296
  god_matches_won: 259
  god_matches_played: 463
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Berserker''s Shield, Breastplate of Valor, Draconic
    Scale, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, The Crusher, Jotunn''s
    Revenge, Eye of Providence, Golden Blade, Oni Hunter''s Garb, Hydra''s Lament,
    Eye of the Storm, Pharaoh''s Curse, Lernaean Bow, Freya''s Tears, Avenging Blade,
    Shield Splitter, Death Metal, Yogi''s Necklace, Spectral Armor, Shield of the
    Phoenix, Shogun''s Ofuda, Erosion, Damaru, Rod of Asclepius, Soul Gem, Dominance,
    Triton''s Conch, Leviathan''s Hide, Bragi''s Harp, Tyrfing, Jade Scepter, Midgardian
    Mail, The Reaper, Wyrmskin Hide, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.54
      pick: 0.18
      fit: 0.17
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.62
      pick: 0.07
      fit: 0.17
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.56
      pick: 0.07
      fit: 0.56
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.37
      fit: 0.45
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.61
      pick: 0.1
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Berserker''s Shield, Breastplate of
    Valor, Draconic Scale, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Gluttonous Grimoire, Rod of Asclepius, Soul Gem, Oni Hunter''s Garb, The Crusher,
    Freya''s Tears, Jotunn''s Revenge, Golden Blade, Pharaoh''s Curse, The Reaper,
    Eye of the Storm, Shield Splitter, Chandra''s Grace, Hydra''s Lament, Erosion,
    Phoenix Feather, Spectral Armor, Riptalon, Avenging Blade, Lernaean Bow, Yogi''s
    Necklace, Blood-Bound Book, Shogun''s Ofuda, Lifebinder, Bancroft''s Talon, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Damaru, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.62
      pick: 0.07
      fit: 0.2
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.07
      fit: 0.53
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.37
      fit: 0.54
    Draconic Scale:
      total: 0.54
      efficiency: 0.5
      win: 0.61
      pick: 0.1
      fit: 0.54
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Breastplate
    of Valor, Runeforged Hammer, Berserker''s Shield, Avenging Blade, Soul Gem, Amanita
    Charm, Kinetic Cuirass, Spear of the Magus, The Reaper, Eye of Providence, Oni
    Hunter''s Garb, The Cosmic Horror, Hydra''s Lament, Riptalon, Void Shield, Heartseeker,
    Golden Blade, Silverbranch Bow, Stone of Binding, Tekko-Kagi, Freya''s Tears,
    Lernaean Bow, Screeching Gargoyle, Pharaoh''s Curse, Void Stone, Yogi''s Necklace,
    Spear of Desolation, Obsidian Shard, Eye of the Storm, Death Metal, Spectral Armor,
    Titan''s Bane, Shield Splitter, Shield of the Phoenix, Damaru.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.54
      pick: 0.18
      fit: 0.12
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.62
      pick: 0.07
      fit: 0.12
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.6
      win: 0.56
      pick: 0.07
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Riptalon
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Breastplate of Valor, Runeforged Hammer, Golden
    Blade, Gluttonous Grimoire, Amanita Charm, Riptalon, Pharaoh''s Curse, Kinetic
    Cuirass, The Crusher, Lernaean Bow, Eye of Providence, Tyrfing, Oni Hunter''s
    Garb, Jotunn''s Revenge, Silverbranch Bow, Shogun''s Ofuda, Hydra''s Lament, Freya''s
    Tears, Soul Gem, Yogi''s Necklace, Dominance, Bracer of The Abyss, Spectral Armor,
    Bragi''s Harp, Shield of the Phoenix, Death Metal, Eros'' Bow, Avenging Blade,
    Eye of the Storm, Toxic Blade, Rod of Asclepius, Shield Splitter, Damaru, Erosion,
    Leviathan''s Hide, Jade Scepter, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.54
      pick: 0.18
      fit: 0.11
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.62
      pick: 0.07
      fit: 0.11
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.6
      win: 0.56
      pick: 0.07
      fit: 0.36
    Riptalon:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Jotunn''s Revenge,
    Freya''s Tears, Soul Gem, Hydra''s Lament, Berserker''s Shield, Runeforged Hammer,
    Gluttonous Grimoire, Shield of the Phoenix, Amanita Charm, Kinetic Cuirass, Chronos''
    Pendant, Eye of Providence, The Crusher, Oni Hunter''s Garb, Chandra''s Grace,
    Spear of Desolation, Screeching Gargoyle, Pharaoh''s Curse, Yogi''s Necklace,
    Gem of Focus, Arondight, Rod of Asclepius, Golden Blade, Spectral Armor, Death
    Metal, Lernaean Bow, Gladiator''s Shield, Jade Scepter, Spear of the Magus, Eye
    of the Storm, Helm of Radiance, Avenging Blade, Shogun''s Ofuda, Erosion, Shield
    Splitter, Leviathan''s Hide, Prophetic Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.18
      fit: 0.44
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.07
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.53
      pick: 0.05
      fit: 0.52
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Runeforged Hammer,
    Gluttonous Grimoire, Kinetic Cuirass, The Crusher, Jotunn''s Revenge, Eye of Providence,
    Golden Blade, Oni Hunter''s Garb, Hydra''s Lament, Eye of the Storm, Pharaoh''s
    Curse, Lernaean Bow, Avenging Blade, Shield Splitter, Death Metal, Yogi''s Necklace,
    Spectral Armor, Shield of the Phoenix, Breastplate of Valor, Shogun''s Ofuda,
    Erosion, Freya''s Tears, Damaru, Rod of Asclepius, Soul Gem, Dominance, Draconic
    Scale, Triton''s Conch, Leviathan''s Hide, Bragi''s Harp, Tyrfing, Jade Scepter,
    Midgardian Mail, Hide of the Nemean Lion, The Reaper, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.56
      pick: 0.07
      fit: 0.56
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
---
