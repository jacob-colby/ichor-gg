---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.65
  slot_order:
  - name: Transcendence
    pick_rate: 0.32
    win_rate: 0.47
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.28
      win_rate: 0.61
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.33
  - name: Dagger of Frenzy
    pick_rate: 0.16
    win_rate: 0.63
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.15
      win_rate: 0.38
    - name: Book of Thoth
      pick_rate: 0.11
      win_rate: 0.58
  - name: The Executioner
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.65
    - name: Polynomicon
      pick_rate: 0.09
      win_rate: 0.36
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: The Executioner
      pick_rate: 0.13
      win_rate: 0.62
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.18
  - name: Silverbranch Bow
    pick_rate: 0.1
    win_rate: 0.73
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.36
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.75
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.55
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.44
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.22
    win_rate: 0.66
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.53
  - name: Archmage's Gem
    pick_rate: 0.1
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-10-27'
  god_win_rate: 0.522633744855967
  god_matches_won: 127
  god_matches_played: 243
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-27'
  god_matches_analyzed: 7385
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Riptalon
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Soul Gem, Riptalon, Lernaean Bow, Tekko-Kagi,
    Tyrfing, The Reaper, Gluttonous Grimoire, Bragi''s Harp, Spear of the Magus, Deathbringer,
    Hydra''s Lament, Golden Blade, Spear of Desolation, Dominance, Demon Blade, Titan''s
    Bane, The Crusher, Bracer of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom
    Orb, Damaru, Rage, The World Stone, Blood-Bound Book, Ancient Signet, Runeforged
    Hammer, Arondight, Avatar''s Parashu, Dreamer''s Idol, Qin''s Blade, Chronos''
    Pendant, Pendulum Blade, Bancroft''s Talon.'
  slot_scores:
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.48
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.45
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.53
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of Desolation, Spear
    of the Magus, Hydra''s Lament, Bragi''s Harp, Lernaean Bow, The Reaper, Tyrfing,
    Tekko-Kagi, Doom Orb, Ancient Signet, Riptalon, The World Stone, Bracer of The
    Abyss, Chronos'' Pendant, Dominance, Deathbringer, Bancroft''s Talon, Titan''s
    Bane, Blood-Bound Book, The Crusher, Dreamer''s Idol, Golden Blade, Arondight,
    Gem of Focus, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Soul Reaver, Pendulum Blade, Polynomicon.'
  slot_scores:
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.42
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.31
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.55
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.35
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.54
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Death Metal
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Deathbringer
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Death Metal, Nimble Ring, Soul Gem, Riptalon, Gluttonous Grimoire, Lernaean
    Bow, The Reaper, Tekko-Kagi, Tyrfing, Deathbringer, Spear of the Magus, Spear
    of Desolation, Bragi''s Harp, Demon Blade, Hydra''s Lament, Golden Blade, Dominance,
    Musashi''s Dual Swords, Titan''s Bane, The Crusher, Bracer of The Abyss, Toxic
    Blade, Doom Orb, Damaru, Rage, The World Stone, Blood-Bound Book, Ancient Signet,
    Dreamer''s Idol, Chronos'' Pendant, Avatar''s Parashu, Runeforged Hammer, Arondight,
    Qin''s Blade, Bancroft''s Talon, Pendulum Blade.'
  slot_scores:
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.49
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.44
    Demon Blade:
      total: 0.49
      efficiency: 0.38
      win: 0.56
      pick: 0.0
      fit: 0.67
    Deathbringer:
      total: 0.5
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.44
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.5
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.2
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Nimble Ring, Death Metal, Gluttonous Grimoire, Spear of Desolation,
    Spear of the Magus, The Reaper, Riptalon, Tekko-Kagi, Hydra''s Lament, Lernaean
    Bow, Bragi''s Harp, Tyrfing, Doom Orb, Chronos'' Pendant, The World Stone, Titan''s
    Bane, The Crusher, Bracer of The Abyss, Dreamer''s Idol, Deathbringer, Ancient
    Signet, Blood-Bound Book, Pendulum Blade, Dominance, Golden Blade, Arondight,
    Gem of Focus, Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual
    Swords, The Cosmic Horror, Demon Blade, Runeforged Hammer, Rod of Asclepius.'
  slot_scores:
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.43
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.46
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.41
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.53
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.33
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, The Reaper, Riptalon,
    Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius, Nimble Ring, Death
    Metal, Kinetic Cuirass, Runeforged Hammer, Golden Blade, Freya''s Tears, Genji''s
    Guard, Blood-Bound Book, Breastplate of Valor, Ethereal Staff, Yogi''s Necklace,
    Shifter''s Shield, Shield Splitter, Bancroft''s Talon, Lernaean Bow, Pharaoh''s
    Curse, Eye of the Storm, Tyrfing, Shogun''s Ofuda, Phoenix Feather, Spear of the
    Magus, Lifebinder, Tekko-Kagi, Erosion, Helm of Radiance, Hydra''s Lament, Eye
    of Providence, Daybreak Gavel, Toxic Blade, Chandra''s Grace.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.3
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.42
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.14
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.63
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Death Metal
  - Silverbranch Bow
  - Tekko-Kagi
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Nimble Ring, Gluttonous Grimoire, Riptalon, Death Metal,
    The Reaper, Tekko-Kagi, Spear of the Magus, Spear of Desolation, Titan''s Bane,
    Lernaean Bow, The Crusher, Tyrfing, Doom Orb, Avenging Blade, Toxic Blade, The
    World Stone, Hydra''s Lament, Dreamer''s Idol, Bragi''s Harp, Deathbringer, Avatar''s
    Parashu, Dominance, Golden Blade, Pendulum Blade, Bracer of The Abyss, Demon Blade,
    Musashi''s Dual Swords, The Cosmic Horror, Oath-Sworn Spear, Ancient Signet, Blood-Bound
    Book, Runeforged Hammer, Chronos'' Pendant, Arondight.'
  slot_scores:
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.61
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.55
    Tekko-Kagi:
      total: 0.52
      efficiency: 0.49
      win: 0.56
      pick: 0.0
      fit: 0.65
    Heartseeker:
      total: 0.61
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.65
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.35
    Soul Gem:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Book of Thoth
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Riptalon
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Death Metal, Riptalon, Tyrfing, Soul Gem, Lernaean Bow,
    Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus,
    Bragi''s Harp, Spear of Desolation, Toxic Blade, Hydra''s Lament, Deathbringer,
    Dominance, Bracer of The Abyss, Qin''s Blade, Demon Blade, Titan''s Bane, The
    Crusher, Musashi''s Dual Swords, Doom Orb, Ancient Signet, The World Stone, Blood-Bound
    Book, Chronos'' Pendant, Dreamer''s Idol, Sun Beam Bow, Runeforged Hammer, Arondight,
    Damaru, Bancroft''s Talon, Rage, Berserker''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.58
      pick: 0.15
      fit: 0.04
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.36
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.56
      pick: 0.0
      fit: 0.6
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.52
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.45
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.17
  community_ordered:
  - Book of Thoth
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Hydra's Lament
  - Spear of Desolation
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Spear of Desolation,
    Death Metal, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear of
    the Magus, Riptalon, Lernaean Bow, The Reaper, Tyrfing, Arondight, Gem of Focus,
    Tekko-Kagi, Bragi''s Harp, Bracer of The Abyss, Pendulum Blade, Deathbringer,
    Doom Orb, Ancient Signet, Dominance, Blood-Bound Book, The World Stone, Golden
    Blade, Titan''s Bane, Totem of Death, The Crusher, Dreamer''s Idol, Breastplate
    of Valor, Toxic Blade, Bancroft''s Talon, Musashi''s Dual Swords, Demon Blade,
    Genji''s Guard, Qin''s Blade.'
  slot_scores:
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.48
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.34
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.4
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Death Metal
  - Spear of Desolation
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Death Metal
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Nimble Ring, Soul Gem, Death Metal, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Lernaean Bow,
    The Reaper, Riptalon, Hydra''s Lament, Bracer of The Abyss, Chronos'' Pendant,
    Tekko-Kagi, Tyrfing, Doom Orb, The World Stone, Ancient Signet, Blood-Bound Book,
    Dreamer''s Idol, Deathbringer, Gem of Focus, Titan''s Bane, Bancroft''s Talon,
    The Crusher, Dominance, Golden Blade, Arondight, Rod of Asclepius, Musashi''s
    Dual Swords, The Cosmic Horror, Demon Blade, Toxic Blade, Pendulum Blade, Typhon’s
    Heart, Polynomicon.'
  slot_scores:
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.51
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.45
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.35
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.47
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.34
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Death Metal
  - Silverbranch Bow
  - Spear of the Magus
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of the Magus
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Spear of the Magus, Spear of Desolation, Bragi''s Harp, The
    Reaper, Lernaean Bow, Tekko-Kagi, Riptalon, Tyrfing, Bracer of The Abyss, Hydra''s
    Lament, Doom Orb, Deathbringer, The World Stone, Titan''s Bane, The Crusher, Ancient
    Signet, Dominance, Golden Blade, Dreamer''s Idol, Blood-Bound Book, Chronos''
    Pendant, Demon Blade, Musashi''s Dual Swords, Bancroft''s Talon, Toxic Blade,
    Runeforged Hammer, Avatar''s Parashu, Arondight, Gem of Focus, The Cosmic Horror,
    Rod of Asclepius.'
  slot_scores:
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.55
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.73
      pick: 0.22
      fit: 0.39
    Spear of the Magus:
      total: 0.51
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.33
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.17
      fit: 0.53
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.33
    Soul Gem:
      total: 0.53
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Silverbranch Bow
  - Heartseeker
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Lernaean Bow
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
    Underrated for this god: Nimble Ring, Death Metal, Soul Gem, Riptalon, Lernaean
    Bow, Tekko-Kagi, Tyrfing, The Reaper, Gluttonous Grimoire, Bragi''s Harp, Spear
    of the Magus, Deathbringer, Hydra''s Lament, Golden Blade, Spear of Desolation,
    Dominance, Demon Blade, Titan''s Bane, The Crusher, Bracer of The Abyss, Musashi''s
    Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, The World Stone, Blood-Bound
    Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s
    Idol, Qin''s Blade, Chronos'' Pendant, Pendulum Blade, Bancroft''s Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.38
      pick: 0.2
      fit: 0.37
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.56
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Jotunn's Revenge
  - Rod of Tahuti
  starter: *id001
---
